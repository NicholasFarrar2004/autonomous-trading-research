import unittest,tempfile,json
from pathlib import Path
from unittest.mock import patch
import run_batch
from operate import cycle_suffix,Journal
class BatchTests(unittest.TestCase):
 def test_cycle_scope_and_original_key(self):
  self.assertEqual(cycle_suffix(),'')
  self.assertEqual(len({cycle_suffix('batch-test',i) for i in range(1,11)}),10)
  for a,b in [('batch-test',0),('batch-test',11),('../escape',1),(None,1),('batch-test',True)]:
   with self.assertRaises(ValueError):cycle_suffix(a,b)
 def test_restart_keeps_same_claim(self):
  with tempfile.TemporaryDirectory() as t:
   j=Journal(Path(t)/'journal.db');key=cycle_suffix('batch-test',1)
   self.assertTrue(j.claim(key));self.assertFalse(j.claim(key));self.assertTrue(j.claim(cycle_suffix('batch-test',2)))
 def test_duplicate_and_nonflat_fail(self):
  for result in [{'clean_exit':False},{'clean_exit':True,'failure':'uncertain'},{'clean_exit':True,'fresh_claim':True,'orders':[]}]:
   with self.assertRaises(RuntimeError):run_batch.check_cycle(result,True)
 def test_rejection_and_unexpected_error_fail(self):
  for result in [{'clean_exit':True,'orders':[{'terminal':True,'status':'Inactive'}]}, {'clean_exit':True,'errors':[{'code':201}]}]:
   with self.assertRaises(RuntimeError):run_batch.check_cycle(result)
 def test_unfilled_terminal_is_not_completion(self):
  self.assertFalse(run_batch.check_cycle({'clean_exit':True,'orders':[{'terminal':True,'status':'Cancelled','filled':0}]}))
 def test_stop_blocks_child_and_restores(self):
  with tempfile.TemporaryDirectory() as t:
   state=Path(t);(state/'STOP').touch()
   with patch.object(run_batch,'STATE',state),patch.object(run_batch,'ROOT',state),patch.object(run_batch.subprocess,'run') as child:
    r=run_batch.run('batch-test',10,True)
    child.assert_not_called();self.assertIn('STOP',r['failure']);self.assertTrue((state/'STOP').exists())
 def test_plan_does_not_execute(self):
  with patch.object(run_batch.subprocess,'run') as child:
   self.assertEqual(run_batch.run('batch-test',10)['max_order_attempts'],20);child.assert_not_called()
if __name__=='__main__':unittest.main()
