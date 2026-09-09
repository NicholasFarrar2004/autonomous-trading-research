"""At most ten real-code paper round trips; sequential processes, no forced fills."""
import argparse,json,os,subprocess,sys,time,fcntl
from pathlib import Path
from operate import cycle_suffix,STATE,ROOT
ALLOWED_STATUS={'Filled','Cancelled','ApiCancelled'}

def check_cycle(result,duplicate=False):
 if result.get('failure') or not result.get('clean_exit'):raise RuntimeError('Cycle did not establish a clean exit')
 if duplicate and (result.get('fresh_claim') or result.get('orders')):raise RuntimeError('Duplicate cycle attempted new orders')
 for order in result.get('orders',[]):
  if not order.get('terminal') or order['status'] not in ALLOWED_STATUS:raise RuntimeError('Abnormal order outcome')
 # Ignore only observed informational connectivity and delayed-data notices.
 if any(e['code'] not in (2104,2106,2107,2108,2119,2158,10167) for e in result.get('errors',[])):
  raise RuntimeError('Unexpected broker error requires review')
 return len(result.get('orders',[]))==2 and all(o['filled']==1 for o in result['orders'])

def run(batch_id,cycles,execute=False):
 if type(cycles) is not int or not 1<=cycles<=10:raise ValueError('At most ten cycles')
 cycle_suffix(batch_id,cycles)
 if not execute: return {'mode':'plan','batch_id':batch_id,'cycles':cycles,'max_order_attempts':cycles*2,'max_position':1}
 STATE.mkdir(parents=True,exist_ok=True)
 lock=(STATE/'batch.lock').open('a');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
 out={'batch_id':batch_id,'requested_round_trips':cycles,'cycles':[],'duplicate_checks':[],'completed_round_trips':0,'started_at':time.time()}
 def invoke(cycle):
  process=subprocess.run([sys.executable,str(Path(__file__).with_name('operate.py')),'--execute','--batch-id',batch_id,'--cycle',str(cycle)],capture_output=True,text=True)
  lines=[x for x in process.stdout.splitlines() if x.startswith('{')]
  if not lines:raise RuntimeError('Child returned no structured result; preserve journal and reconcile')
  result=json.loads(lines[-1])
  return result
 try:
  if (STATE/'STOP').exists():raise RuntimeError('STOP is active; no batch entry permitted')
  for cycle in range(1,cycles+1):
   if (STATE/'STOP').exists():raise RuntimeError('Batch stopped before next cycle')
   result=invoke(cycle);out['cycles'].append(result)
   complete=check_cycle(result);out['completed_round_trips']+=int(complete)
   duplicate=invoke(cycle);out['duplicate_checks'].append(duplicate);check_cycle(duplicate,True)
   (ROOT/('batch-'+batch_id+'-result.json')).write_text(json.dumps(out,indent=2))
   print(json.dumps({'cycle':cycle,'completed':complete,'total_completed':out['completed_round_trips'],'duplicate_new_orders':len(duplicate['orders']),'flat':True}),flush=True)
 except BaseException as e:
  out['failure']=str(e)
 finally:
  (STATE/'STOP').write_text('Bounded batch exited. Entry disabled; reconcile before intentional resumption.\n')
  out['finished_at']=time.time();(ROOT/('batch-'+batch_id+'-result.json')).write_text(json.dumps(out,indent=2))
  fcntl.flock(lock,fcntl.LOCK_UN);lock.close()
 return out
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--batch-id',required=True);p.add_argument('--cycles',type=int,default=10);p.add_argument('--execute',action='store_true');a=p.parse_args();r=run(a.batch_id,a.cycles,a.execute)
 print(json.dumps({'requested':r.get('requested_round_trips'),'completed':r.get('completed_round_trips'),'failure':r.get('failure'),'stop_restored':(STATE/'STOP').exists()}),flush=True)
 sys.exit(1 if r.get('failure') else 0)
