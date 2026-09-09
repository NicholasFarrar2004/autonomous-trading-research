import os,json,logging
from pathlib import Path
from project_paths import DATA, STATE, PRIVATE
os.environ['PYSYS_PRIVATE_CONFIG_DIR']=str(PRIVATE)
from sysbrokers.IB.ib_connection import connectionIB
from sysbrokers.IB.paper_guard import PaperGuardError
from ib_async import Future,LimitOrder
DATA.mkdir(parents=True,exist_ok=True)
logging.disable(logging.CRITICAL)
c=connectionIB(client_id=105)
try:
 ib=c.ib;ib.RequestTimeout=20
 p=ib.reqPositions();o=ib.reqAllOpenOrders()
 blocked=False
 try:ib.placeOrder(Future('MES',exchange='CME'),LimitOrder('BUY',1,1))
 except PaperGuardError:blocked=True
 out={'independent_client':105,'server_time':str(ib.reqCurrentTime()),'nonzero_positions':sum(1 for x in p if x.position),'open_orders':len(o),'default_write_guard_blocks_before_broker':blocked,'account_exactly_verified_by_connection':True}
 (DATA/(Path(__file__).stem+'.json')).write_text(json.dumps(out,indent=2));print(json.dumps(out))
finally:c.close_connection()
