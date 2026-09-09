"""Bounded read-only native IB snapshot, no order submission or write lease."""
import argparse, json, logging, os, re, socket
from datetime import datetime, timezone
from pathlib import Path

def capture(private_dir,out):
    result={'observed_at':datetime.now(timezone.utc).isoformat(),'orders_sent':0,
            'mode':'paper-read-only','broker_state_verified':False}
    try:
        with socket.create_connection(('127.0.0.1',4002),timeout=3):pass
    except OSError:
        result['blocker']='Paper Gateway is not listening on localhost4002; no broker position claim made.'
    else:
        os.environ['PYSYS_PRIVATE_CONFIG_DIR']=str(private_dir)
        logging.disable(logging.CRITICAL)
        from sysbrokers.IB.ib_connection import connectionIB
        c=None
        try:
            c=connectionIB(client_id=109);ib=c.ib;ib.RequestTimeout=20
            positions=ib.reqPositions();orders=ib.reqAllOpenOrders()
            result.update(broker_state_verified=True,
                          nonzero_positions=sum(bool(p.position) for p in positions),
                          open_orders=len(orders),server_time=str(ib.reqCurrentTime()))
        except Exception as exc:
            result['blocker']=re.sub(r'\b[UD][A-Z]*[0-9]+\b','[account redacted]',str(exc))
        finally:
            if c is not None:c.close_connection()
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2));return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--private-dir',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();print(json.dumps(capture(a.private_dir,a.out),indent=2))
