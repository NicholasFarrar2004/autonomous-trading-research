import unittest,tempfile,copy,sqlite3
from pathlib import Path
from types import SimpleNamespace as NS
from unittest.mock import Mock,patch
import pandas as pd
from ib_async import Future,LimitOrder
from sysbrokers.IB.paper_guard import BoundedPaperLease,PaperGuardError,ReadOnlyPaperIB
from native_signal import validate_history
from synthetic_fixture import synthetic_history
from operate import Journal
class Tests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.stop=Path(self.tmp.name)/'STOP'
  self.lease=BoundedPaperLease('DU12345678',123,1,self.stop)
  self.ib=NS(managedAccounts=lambda:['DU12345678'],isConnected=lambda:True,client=NS(host='127.0.0.1',port=4002))
  self.contract=Future('MES',exchange='CME',currency='USD',multiplier='5',conId=123)
  self.order=LimitOrder('BUY',1,7500,account='DU12345678',tif='IOC',orderRef='workos-paper-test-entry')
  self.lease.arm_intent(self.order.orderRef,'entry',0,7500)
 def tearDown(self):self.tmp.cleanup()
 def test_single_send_consumes_intent_before_network(self):
  self.lease.validate(self.ib,self.contract,self.order)
  with self.assertRaises(PaperGuardError):self.lease.validate(self.ib,self.contract,self.order)
 def test_wrong_account_endpoint_contract(self):
  for key,value in [('conId',124),('secType','CONTFUT'),('symbol','ES'),('currency','EUR'),('multiplier','50')]:
   c=copy.copy(self.contract);setattr(c,key,value)
   with self.subTest(key=key),self.assertRaises(PaperGuardError):self.lease.validate(self.ib,c,self.order)
  self.ib.client.port=4001
  with self.assertRaises(PaperGuardError):self.lease.validate(self.ib,self.contract,self.order)
  self.ib.client.port=4002;self.ib.managedAccounts=lambda:['U12345678']
  with self.assertRaises(PaperGuardError):self.lease.validate(self.ib,self.contract,self.order)
 def test_order_scope(self):
  for key,value in [('totalQuantity',2),('orderType','MKT'),('tif','DAY'),('action','SELL'),('account','U12345678'),('lmtPrice',8000),('orderRef','other')]:
   o=copy.copy(self.order);setattr(o,key,value)
   with self.subTest(key=key),self.assertRaises(PaperGuardError):self.lease.validate(self.ib,self.contract,o)
 def test_stop_and_expiry(self):
  self.stop.touch()
  with self.assertRaises(PaperGuardError):self.lease.validate(self.ib,self.contract,self.order)
  self.stop.unlink();self.lease.deadline=0
  with self.assertRaises(PaperGuardError):self.lease.validate(self.ib,self.contract,self.order)
 def test_cleanup_allowed_after_stop_only_reducing(self):
  self.lease.validate(self.ib,self.contract,self.order);self.stop.touch();self.lease.deadline=0
  with self.assertRaises(PaperGuardError):self.lease.arm_intent('workos-paper-cleanup','cleanup',0,7500)
  self.lease.arm_intent('workos-paper-cleanup','cleanup',1,7500)
  self.order.orderRef='workos-paper-cleanup';self.order.action='SELL'
  self.lease.validate(self.ib,self.contract,self.order)
  with self.assertRaises(PaperGuardError):self.lease.arm_intent('workos-paper-third','cleanup',1,7500)
 def test_default_read_only_remains(self):
  ib=ReadOnlyPaperIB()
  for fn,args in [(ib.placeOrder,(self.contract,self.order)),(ib.cancelOrder,(self.order,)),(ib.reqGlobalCancel,())]:
   with self.assertRaises(PaperGuardError):fn(*args)
 def test_durable_claim_and_intent_survive_restart(self):
  p=Path(self.tmp.name)/'journal.db';j=Journal(p);self.assertTrue(j.claim('same'))
  ref=j.intent('same','entry',{'intent':'before network'});j.db.close();j=Journal(p)
  self.assertFalse(j.claim('same'));self.assertEqual(j.refs('same'),[(ref,'entry')])
  with self.assertRaises(sqlite3.IntegrityError):j.intent('same','entry',{})
 def test_history_rejects_material_faults(self):
  good=synthetic_history();validate_history(good)
  for case in ['short','volume','duplicate','negative','ohlc','nan']:
   f=good.copy()
   if case=='short':f=f.tail(100)
   elif case=='volume':f.VOLUME=0
   elif case=='duplicate':f.index=[f.index[0]]*len(f)
   elif case=='negative':f.iloc[0,0]=-1
   elif case=='ohlc':f.iloc[0,f.columns.get_loc('HIGH')]=1
   elif case=='nan':f.iloc[0,0]=float('nan')
   with self.subTest(case=case),self.assertRaises(ValueError):validate_history(f)
if __name__=='__main__':unittest.main()
