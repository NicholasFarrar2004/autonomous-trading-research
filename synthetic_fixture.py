"""Fictional fixtures for offline tests. Never broker identities or market history."""
from pathlib import Path
from datetime import datetime,timedelta
from zoneinfo import ZoneInfo

def synthetic_profile(base=Path('/tmp/fictional-paper-tests')):
 root=Path(base).resolve()/'paper'
 result={'paper_environment':'paper-read-only','broker_account':None,'paper_account_allowlist':[],
         'ib_ipaddress':'127.0.0.1','ib_port':4002,'paper_state_root':str(root),
         'mongo_db':'pysystemtrade_paper','mongo_host':'127.0.0.1','mongo_dump_all':False}
 for key,leaf in [('parquet_store','parquet'),('backtest_store_directory','backtests'),('csv_backup_directory','csv-backups'),('mongo_dump_directory','mongo-dump'),('echo_directory','echo')]:result[key]=str(root/leaf)
 return result

def synthetic_history():
 import numpy as np
 import pandas as pd
 end=datetime.now(ZoneInfo('America/New_York')).date()-timedelta(days=1)
 dates=pd.bdate_range(end=end,periods=251)
 t=np.arange(len(dates));price=100+t*.03+np.sin(t/3)
 return pd.DataFrame({'OPEN':price,'HIGH':price+1,'LOW':price-1,'FINAL':price+.1,'VOLUME':100},index=dates)
