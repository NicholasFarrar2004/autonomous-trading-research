import tempfile, unittest
from pathlib import Path
import pandas as pd
from evaluate_strategy import account
from forward_plan import ForwardJournal, RecoveryRequired, plan_transition, observe_history

class Accounting(unittest.TestCase):
    def test_lag_and_boundary_costs_by_hand(self):
        idx=pd.bdate_range('2024-01-01',periods=6)
        p=pd.Series([100,200,300,310,320,330],index=idx)
        t=pd.Series([1,1,0,0,0,0],index=idx)
        result,d=account(p,t,pd.Series(False,index=idx),side_cost=2,monthly_cost=0,delay=2)
        # Enter close300; exit close320. No profit from prices100->300.
        self.assertEqual(result['gross_proxy_usd'],100)
        self.assertEqual(result['execution_cost_usd'],4)
        self.assertEqual(result['modeled_net_usd'],96)
        self.assertEqual(result['boundary_liquidation_sides'],0)
    def test_roll_charge_and_short_sign(self):
        idx=pd.bdate_range('2024-01-01',periods=5)
        p=pd.Series([100,100,100,90,80],index=idx)
        t=pd.Series(-1,index=idx);r=pd.Series([0,0,0,1,0],index=idx)
        result,_=account(p,t,r,side_cost=2,monthly_cost=0)
        self.assertEqual(result['gross_proxy_usd'],100)
        self.assertEqual(result['roll_sides'],2)
        self.assertEqual(result['execution_cost_usd'],8) # entry, boundary, roll pair
        self.assertEqual(result['completed_rule_episodes'],0)
    def test_initial_equity_drawdown_and_cost_monotonicity(self):
        idx=pd.bdate_range('2024-01-01',periods=5)
        p=pd.Series([100,100,100,90,80],index=idx);t=pd.Series(1,index=idx);r=pd.Series(False,index=idx)
        low,_=account(p,t,r,1,0);high,_=account(p,t,r,5,100)
        self.assertGreaterEqual(low['max_drawdown_usd'],100)
        self.assertLess(high['modeled_net_usd'],low['modeled_net_usd'])

class Recovery(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.path=Path(self.tmp.name)/'journal.sqlite3';self.j=ForwardJournal(self.path)
    def tearDown(self):self.j.db.close();self.tmp.cleanup()
    def test_pending_before_send_survives_restart_and_no_evidence_never_retries(self):
        self.j.claim_intent('first',0,1,10);self.j.db.close();self.j=ForwardJournal(self.path)
        with self.assertRaises(RecoveryRequired):self.j.claim_intent('next',0,1,20)
        with self.assertRaises(RecoveryRequired):self.j.reconcile('first',position=0,executions=[],open_refs=[],snapshot_time=20,evidence_complete=True)
    def test_partial_fill_halts_then_complete_deduplicated_fill_reconciles(self):
        self.j.claim_intent('first',0,1,10)
        f={'ref':'first','execution_id':'a','direction':1,'quantity':.5}
        with self.assertRaises(RecoveryRequired):self.j.reconcile('first',position=.5,executions=[f],open_refs=[],snapshot_time=20,evidence_complete=True)
        g={**f,'execution_id':'b'}
        self.assertEqual(self.j.reconcile('first',position=1,executions=[f,g,f],open_refs=[],snapshot_time=20,evidence_complete=True),'reconciled')
        self.assertEqual(self.j.reconcile('first',position=1,executions=[],open_refs=[],snapshot_time=20,evidence_complete=True),'reconciled')
    def test_stale_open_incomplete_and_mismatched_evidence_halt(self):
        self.j.claim_intent('first',0,1,10)
        base=dict(position=1,executions=[{'ref':'first','execution_id':'a','direction':1,'quantity':1}],open_refs=[],snapshot_time=20,evidence_complete=True)
        for change in ({'snapshot_time':9},{'open_refs':['first']},{'evidence_complete':False},{'position':0},{'executions':[{**base['executions'][0],'direction':-1}]}):
            with self.subTest(change=change),self.assertRaises(RecoveryRequired):self.j.reconcile('first',**{**base,**change})
    def test_same_date_revision_and_duplicate(self):
        self.assertTrue(self.j.observe('2024-01-01',{'target':1}))
        self.assertFalse(self.j.observe('2024-01-01',{'target':1}))
        with self.assertRaises(RecoveryRequired):self.j.observe('2024-01-01',{'target':0})
    def test_actual_native_shadow_normalizes_close_times_and_rejects_stale(self):
        from synthetic_fixture import synthetic_history
        from datetime import datetime, timedelta
        from zoneinfo import ZoneInfo
        f=synthetic_history();f.index=f.index+pd.Timedelta(hours=23)
        p=Path(self.tmp.name)/'history.parquet';f.to_parquet(p)
        out=Path(self.tmp.name)/'shadow'
        first=observe_history(p,out)
        self.assertTrue(first['fresh_observation'])
        self.assertIn(first['desired_target'],(-1,0,1))
        self.assertFalse(observe_history(p,out)['fresh_observation'])
        with self.assertRaises(ValueError):
            observe_history(p,out,datetime.now(ZoneInfo('America/New_York'))+timedelta(days=10))
    def test_no_forced_cleanup_and_reversal_is_sequenced(self):
        self.assertEqual(plan_transition(1,1)['action'],'HOLD')
        self.assertEqual(plan_transition(0,0)['action'],'FLAT')
        self.assertEqual(plan_transition(1,-1)['action'],'CLOSE_THEN_RECONCILE')
        self.assertEqual(plan_transition(0,1)['action'],'BLOCKED_ENTRY')
        self.assertEqual(plan_transition(1,1,expiry_days=6)['action'],'RECOVERY_REQUIRED')
        with self.assertRaises(RecoveryRequired):plan_transition(1,0,open_orders=1)

if __name__=='__main__':unittest.main()
