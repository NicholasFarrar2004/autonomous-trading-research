"""Bounded native IB paper exercise. Default is read-only preparation.

--execute is a deliberate one-shot capability; persisted date/strategy claim prevents
repeat entry. IOC limits, own-order cancellation, exact-account position checks.
"""
import os,json,logging,sqlite3,fcntl,time,math,hashlib,re,sys
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from project_paths import DATA, STATE, PRIVATE
os.environ['PYSYS_PRIVATE_CONFIG_DIR']=str(PRIVATE)
from native_signal import build_signal
from sysbrokers.IB.ib_connection import connectionIB
from sysbrokers.IB.paper_guard import BoundedPaperLease,PaperGuardError,verify_managed_account
from sysbrokers.IB.client.ib_orders_client import ibOrdersClient
from sysbrokers.IB.ib_instruments import ibInstrumentConfigData,futuresInstrumentWithIBConfigData
from sysobjects.instruments import futuresInstrument
from sysobjects.contracts import futuresContract
from sysexecution.trade_qty import tradeQuantity
from sysexecution.orders.broker_orders import limit_order_type
from ib_async import ExecutionFilter
ROOT=DATA

STATE.mkdir(mode=0o700,parents=True,exist_ok=True)
logging.disable(logging.CRITICAL)

def scrub(value):return re.sub(r'\b[UD][A-Z]*[0-9]+\b','[account redacted]',json.dumps(value,default=str))

class Journal:
 def __init__(self,path):
  self.db=sqlite3.connect(path);os.chmod(path,0o600)
  self.db.execute('PRAGMA synchronous=FULL')
  self.db.execute('CREATE TABLE IF NOT EXISTS runs (key TEXT PRIMARY KEY, phase TEXT NOT NULL)')
  self.db.execute('CREATE TABLE IF NOT EXISTS intents (ref TEXT PRIMARY KEY, key TEXT NOT NULL, phase TEXT NOT NULL, payload TEXT NOT NULL)')
  self.db.execute('CREATE TABLE IF NOT EXISTS events (at TEXT, key TEXT, payload TEXT)');self.db.commit()
 def claim(self,key):
  try:self.db.execute('INSERT INTO runs VALUES (?,?)',(key,'claimed'));self.db.commit();return True
  except sqlite3.IntegrityError:return False
 def intent(self,key,phase,payload):
  ref='workos-paper-'+key[:16]+'-'+phase
  self.db.execute('INSERT INTO intents VALUES (?,?,?,?)',(ref,key,phase,scrub(payload)));self.db.commit();return ref
 def refs(self,key):return self.db.execute('SELECT ref,phase FROM intents WHERE key=?',(key,)).fetchall()
 def event(self,key,value):
  self.db.execute('INSERT INTO events VALUES (?,?,?)',(datetime.now(ZoneInfo('UTC')).isoformat(),key,scrub(value)));self.db.commit()
 def finish(self,key,phase):self.db.execute('UPDATE runs SET phase=? WHERE key=?',(phase,key));self.db.commit()

class NativeIOC(ibOrdersClient):
 def _build_ib_order(self,*args,**kwargs):
  order=super()._build_ib_order(*args,**kwargs)
  order.tif='IOC';order.orderRef=self.current_ref
  return order

def snapshot(ib,account,conid):
 verify_managed_account(ib,account)
 positions=ib.reqPositions();orders=ib.reqAllOpenOrders();ib.sleep(1)
 own=[p for p in positions if p.account==account and p.position]
 unrelated=[p for p in own if p.contract.conId!=conid]
 return {'position':sum(p.position for p in own if p.contract.conId==conid),'unrelated_positions':len(unrelated),'open_orders':len(orders)},orders

def quote(ib,contract):
 ib.reqMarketDataType(3);t=ib.reqMktData(contract,'',False,False);ib.sleep(5)
 value={'bid':t.bid,'ask':t.ask,'type':t.marketDataType,'received_at':str(t.time)}
 ib.cancelMktData(contract)
 if not all(math.isfinite(value[x]) and value[x]>0 for x in ('bid','ask')) or value['ask']<value['bid'] or value['ask']-value['bid']>2:
  raise PaperGuardError('Invalid or excessively wide bid/ask')
 return value

def terminal(ib,trade):
 deadline=time.monotonic()+20
 while not trade.isDone() and time.monotonic()<deadline:ib.sleep(.25)
 if not trade.isDone():
  ib.cancelOrder(trade.order)
  deadline=time.monotonic()+10
  while not trade.isDone() and time.monotonic()<deadline:ib.sleep(.25)
 return {'status':trade.orderStatus.status,'filled':trade.orderStatus.filled,'remaining':trade.orderStatus.remaining,'average_fill':trade.orderStatus.avgFillPrice,'terminal':trade.isDone()}

def main(execute=False):
 lock=(STATE/'run.lock').open('a');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
 signal=build_signal();meta=json.loads((ROOT/'fetch_continuous.json').read_text())['contract']
 expiry=datetime.strptime(meta['lastTradeDateOrContractMonth'],'%Y%m%d').date()
 if (expiry-datetime.now(ZoneInfo('America/New_York')).date()).days<7:raise PaperGuardError('Contract too near expiry')
 key=hashlib.sha256((signal['data_date']+'|ewmac8-32_32-128|50000|10|MES|max1|v1').encode()).hexdigest()
 journal=Journal(STATE/'journal.sqlite3');result={'mode':'execute' if execute else 'prepare','signal':signal,'key':key,'orders':[],'errors':[],'delayed_fills_not_profitability_evidence':True}
 c=connectionIB(client_id=104);ib=c.ib;ib.RequestTimeout=20
 ib.errorEvent+=lambda req,code,msg,contract: result['errors'].append({'code':code,'message':msg})
 try:
  instrument=futuresInstrumentWithIBConfigData(futuresInstrument('SP500_micro'),ibInstrumentConfigData('MES','CME','USD',5,1,False))
  native_contract=futuresContract(instrument,meta['lastTradeDateOrContractMonth'])
  client=NativeIOC(c);contract=client.ib_futures_contract_with_legs(native_contract).ibcontract
  if contract.conId!=meta['conId']:raise PaperGuardError('Native contract resolution differs from verified history metadata')
  before,_=snapshot(ib,c.account,contract.conId);result['before']=before
  if before['unrelated_positions'] or before['open_orders']:raise PaperGuardError('Existing unrelated positions or open orders require review')
  result['quote']=quote(ib,contract)
  if not execute:
   result['prepared']=True;result['native_order_preview']={'type':'LMT','tif':'IOC','quantity':1,'direction':signal['bounded_target'],'contract':contract.localSymbol}
   return result
  fresh=journal.claim(key);result['fresh_claim']=fresh
  target=signal['bounded_target']
  if target==0:journal.finish(key,'no_signal');return result
  lease=BoundedPaperLease(c.account,contract.conId,target,STATE/'STOP');ib._bounded_paper_lease=lease
  previous=journal.refs(key);lease.used_refs.update(ref for ref,phase in previous)
  def submit(phase,position):
   q=quote(ib,contract);direction=target if phase=='entry' else -position
   # Deliberately marketable, finite limit for mechanics only, never a return estimate.
   limit=round(((q['ask']+20) if direction>0 else (q['bid']-20))*4)/4
   payload={'position':position,'direction':direction,'limit':limit,'quote':q}
   ref=journal.intent(key,phase,payload);lease.arm_intent(ref,phase,position,limit);client.current_ref=ref
   trade=client.broker_submit_order(native_contract,tradeQuantity([direction]),account_id=c.account,order_type=limit_order_type,limit_price=limit).trade
   outcome=terminal(ib,trade);result['orders'].append({'phase':phase,'ref':ref,**payload,**outcome});journal.event(key,result['orders'][-1])
  if fresh:
   if before['position']!=0:raise PaperGuardError('Initial position is not flat')
   submit('entry',0)
  # Reconnect before authoritative reconciliation; no ambiguous entry resubmission.
  ib.disconnect();ib.connect('127.0.0.1',4002,clientId=104,account=c.account,readonly=True);verify_managed_account(ib,c.account)
  after,orders=snapshot(ib,c.account,contract.conId);result['after_entry_reconnect']=after
  if orders or after['unrelated_positions']:raise PaperGuardError('Open orders or unrelated positions at reconciliation; no further entry')
  if after['position']:
   if after['position']!=target or any(phase=='cleanup' for _,phase in previous):raise PaperGuardError('Unresolved position requires explicit recovery; no blind retry')
   submit('cleanup',after['position'])
  final,orders=snapshot(ib,c.account,contract.conId);result['final']=final
  fills=ib.reqExecutions(ExecutionFilter(clientId=104));ib.sleep(2)
  refs={ref for ref,_ in journal.refs(key)}
  result['fills']=[{'ref':f.execution.orderRef,'execution_id':f.execution.execId,'side':f.execution.side,'quantity':f.execution.shares,'price':f.execution.price,'commission':f.commissionReport.commission,'commission_currency':f.commissionReport.currency,'realized_pnl':f.commissionReport.realizedPNL} for f in fills if f.execution.orderRef in refs]
  result['clean_exit']=final['position']==0 and final['open_orders']==0 and final['unrelated_positions']==0
  if not result['clean_exit']:raise PaperGuardError('Nonflat paper state at exit: needs immediate recovery')
  journal.finish(key,'flat_complete');return result
 except BaseException as e:
  result['failure']=str(e);journal.event(key,result)
  try:result['failure_snapshot'],_=snapshot(ib,c.account,meta['conId'])
  except BaseException:result['failure_snapshot']='unavailable; reconciliation required'
  return result
 finally:
  ib._bounded_paper_lease=None;c.close_connection()
  filename='execution-result.json' if execute else 'preparation-result.json'
  (ROOT/filename).write_text(scrub(result));journal.event(key,result)
  fcntl.flock(lock,fcntl.LOCK_UN);lock.close()
if __name__=='__main__':
 result=main(execute='--execute' in sys.argv);print(scrub(result))
 sys.exit(1 if 'failure' in result else 0)
