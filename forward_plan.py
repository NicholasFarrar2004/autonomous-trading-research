"""Read-only forward decision and crash-recovery ledger. Never submits orders.

A strategy HOLD is preserved; an immediate cleanup is never manufactured.
"""
import argparse, hashlib, json, logging, sqlite3
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo
import pandas as pd
from evaluate_strategy import native_targets
from native_signal import validate_history

class RecoveryRequired(RuntimeError):
    pass

def plan_transition(position, target, *, open_orders=0, unrelated_positions=0,
                    expiry_days=30, stopped=True, quote_fresh=False):
    if type(position) is not int or position not in (-1,0,1):
        raise RecoveryRequired('Fractional or out-of-scope position')
    if type(target) is not int or target not in (-1,0,1):
        raise RecoveryRequired('Invalid target')
    if open_orders or unrelated_positions:
        raise RecoveryRequired('Reconcile orders/unrelated positions before any transition')
    if position and expiry_days < 7:
        return {'action':'RECOVERY_REQUIRED','reason':'Existing exposure inside expiry guard; supervised reducing exit needed'}
    if position == target:
        return {'action':'HOLD' if position else 'FLAT','quantity':0,'target':target}
    if position and target != position:
        return {'action':'CLOSE_THEN_RECONCILE','quantity':1,'direction':-position,
                'deferred_target':target,'reason':'Rule-driven exit or reversal; never submit a two-contract reversal'}
    if stopped or not quote_fresh or expiry_days < 7:
        return {'action':'BLOCKED_ENTRY','quantity':0,'target':target,
                'reason':'STOP, quote freshness or expiry gate'}
    return {'action':'PREVIEW_ENTRY','quantity':1,'direction':target,
            'reason':'No writer in this workflow; bounded supervisor required'}

class ForwardJournal:
    def __init__(self,path):
        path=Path(path);path.parent.mkdir(parents=True,exist_ok=True,mode=0o700)
        self.db=sqlite3.connect(path)
        path.chmod(0o600)
        self.db.execute('PRAGMA synchronous=FULL')
        self.db.execute('CREATE TABLE IF NOT EXISTS observations (day TEXT PRIMARY KEY, digest TEXT, payload TEXT)')
        self.db.execute('CREATE TABLE IF NOT EXISTS pending (ref TEXT PRIMARY KEY, before_pos INTEGER, direction INTEGER, sent_after REAL, status TEXT)')
        self.db.commit()
    def observe(self,day,payload):
        text=json.dumps(payload,sort_keys=True,allow_nan=False)
        digest=hashlib.sha256(text.encode()).hexdigest()
        old=self.db.execute('SELECT digest FROM observations WHERE day=?',(day,)).fetchone()
        if old:
            if old[0]!=digest:raise RecoveryRequired('Same-date observation changed; review data revision before reuse')
            return False
        self.db.execute('INSERT INTO observations VALUES (?,?,?)',(day,digest,text));self.db.commit();return True
    def claim_intent(self,ref,before,direction,now):
        # Future writer integration must invoke this transaction BEFORE network I/O.
        self.db.execute('BEGIN IMMEDIATE')
        try:
            if self.db.execute("SELECT 1 FROM pending WHERE status='pending'").fetchone():
                raise RecoveryRequired('An unresolved intent blocks all new intents')
            if type(before) is not int or before not in (-1,0,1) or direction not in (-1,1) or abs(before+direction)>1:
                raise RecoveryRequired('Intent exceeds one-contract exposure')
            self.db.execute('INSERT INTO pending VALUES (?,?,?,?,?)',(ref,before,direction,now,'pending'))
            self.db.commit()
        except BaseException:
            self.db.rollback();raise
    def reconcile(self,ref,*,position,executions,open_refs,snapshot_time,evidence_complete):
        row=self.db.execute('SELECT before_pos,direction,sent_after,status FROM pending WHERE ref=?',(ref,)).fetchone()
        if not row:raise RecoveryRequired('Unknown intent')
        before,direction,after,status=row
        if status!='pending':return status
        if not evidence_complete or snapshot_time < after or open_refs:
            raise RecoveryRequired('Incomplete/stale snapshot or outstanding orders')
        unique={}
        for fill in executions:
            if fill['ref']!=ref:continue
            key=fill['execution_id']
            if key in unique and unique[key]!=fill:raise RecoveryRequired('Conflicting duplicate execution')
            unique[key]=fill
        for fill in unique.values():
            if fill['direction']!=direction or not 0 < fill['quantity'] <= 1:
                raise RecoveryRequired('Wrong-side or invalid fill')
        quantity=sum(f['quantity'] for f in unique.values())
        if quantity!=1 or position!=before+direction:
            # Even zero orders/fills with original position cannot prove never sent.
            raise RecoveryRequired('Ambiguous/partial submission or position mismatch; no automatic retry')
        self.db.execute("UPDATE pending SET status='reconciled' WHERE ref=?",(ref,));self.db.commit()
        return 'reconciled'

def observe_history(history,out,now=None):
    now=now or datetime.now(ZoneInfo('America/New_York'))
    logging.disable(logging.CRITICAL)
    frame=pd.read_parquet(history)
    # IB daily bars use a close-time index; native daily stages use date labels.
    frame.index=frame.index.normalize()
    # At daytime, only prior completed sessions; refuse today's potentially provisional bar.
    frame=frame.loc[frame.index.date < now.date()]
    validate_history(frame,now)
    targets=native_targets(frame.FINAL,frame.FINAL)
    if len(targets)<203:raise RecoveryRequired('Insufficient history for delayed target')
    decision=targets.iloc[-3] # t+2 close convention, not an order at this morning's quote
    payload={'protocol':'frozen-v1','observed_data_date':str(frame.index[-1].date()),
             'signal_date':str(targets.index[-3].date()),'desired_target':int(decision.target),
             'latest_signal_target':int(targets.target.iloc[-1]),
             'data_sha256':hashlib.sha256(Path(history).read_bytes()).hexdigest(),
             'source':'cached IB normalized continuous series; integration variant only',
             'execution_enabled':False,'broker_state_verified':False,
             'status':'SHADOW_OBSERVATION_ONLY; current broker reconciliation and supervised runtime missing'}
    out.mkdir(parents=True,exist_ok=True)
    j=ForwardJournal(out/'forward.sqlite3');fresh=j.observe(payload['observed_data_date'],payload);j.db.close()
    (out/'latest-observation.json').write_text(json.dumps(payload,indent=2))
    return {'fresh_observation':fresh,**payload}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--history',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();print(json.dumps(observe_history(a.history,a.out),indent=2))
