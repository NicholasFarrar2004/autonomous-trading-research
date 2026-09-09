"""Load the actual native profile. Default command never connects to a broker."""
import argparse
import os
from pathlib import Path

from project_paths import PRIVATE
os.environ['PYSYS_PRIVATE_CONFIG_DIR'] = str(PRIVATE)
from sysdata.config.production_config import get_production_config
from sysbrokers.IB.paper_guard import PaperGuardError, validate_paper_config

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--connect-read-only', action='store_true')
    args = parser.parse_args()
    cfg = get_production_config()
    try:
        validate_paper_config(cfg, cfg.ib_ipaddress, cfg.ib_port, getattr(cfg, 'broker_account', None))
    except PaperGuardError as exc:
        print(f'BLOCKED before connection: {exc}')
        raise SystemExit(2)
    print('Paper configuration preflight passed; no broker identity verified yet.')
    if args.connect_read_only:
        from sysbrokers.IB.ib_connection import connectionIB
        connection = connectionIB(client_id=100)
        try:
            print('Read-only paper account identity verified. No orders enabled.')
        finally:
            connection.close_connection()
