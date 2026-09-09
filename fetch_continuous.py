import os,json,logging,datetime,math
from pathlib import Path
from project_paths import DATA, STATE, PRIVATE
os.environ['PYSYS_PRIVATE_CONFIG_DIR']=str(PRIVATE)
from sysbrokers.IB.ib_connection import connectionIB
from sysbrokers.IB.client.ib_price_client import ibPriceClient
from sysbrokers.IB.ib_instruments import ibInstrumentConfigData,futuresInstrumentWithIBConfigData,ib_futures_instrument
from sysobjects.instruments import futuresInstrument
DATA.mkdir(parents=True,exist_ok=True)
logging.disable(logging.CRITICAL)
out={'scope':'paper-read-only','orders_sent':False,'errors':[]}
c=connectionIB(client_id=103)
try:
 ib=c.ib;ib.RequestTimeout=25
 ib.errorEvent+=lambda req,code,msg,contract: out['errors'].append({'code':code,'message':msg})
 out['server_time']=str(ib.reqCurrentTime())
 client=ibPriceClient(c)
 instrument=futuresInstrumentWithIBConfigData(futuresInstrument('SP500_micro'),ibInstrumentConfigData('MES','CME','USD',5,1,False))
 chain=client.ib_get_contract_chain(ib_futures_instrument(instrument),allow_expired=False)
 out['chain_count']=len(chain)
 chain=sorted([x for x in chain if x.lastTradeDateOrContractMonth>=datetime.date.today().strftime('%Y%m%d')],key=lambda x:x.lastTradeDateOrContractMonth)
 if chain:
  contract=chain[0];out['contract']={k:getattr(contract,k) for k in ['symbol','localSymbol','lastTradeDateOrContractMonth','exchange','currency','multiplier','conId']}
  ib.reqMarketDataType(3)
  ticker=ib.reqMktData(contract,'',False,False)
  ib.sleep(8)
  def finite(x):return x if isinstance(x,(int,float)) and math.isfinite(x) else None
  out['market_data']={'type':ticker.marketDataType,'bid':finite(ticker.bid),'ask':finite(ticker.ask),'last':finite(ticker.last),'time':str(ticker.time)}
  ib.cancelMktData(contract)
  from ib_async import ContFuture
  continuous=ContFuture('MES',exchange='CME',currency='USD')
  bars=client._ib_get_historical_data_of_duration_and_barSize(continuous,durationStr='1 Y',barSizeSetting='1 day')
  out['history']={'rows':0 if bars is None else len(bars),'first':None if bars is None or bars.empty else str(bars.iloc[0]['date']),'last':None if bars is None or bars.empty else str(bars.iloc[-1]['date'])}
  if bars is not None and not bars.empty:
   frame=client._raw_ib_data_to_df(bars);frame.to_parquet(DATA/'continuous-history.parquet');out['native_frame']={'rows':len(frame),'columns':list(frame.columns),'duplicates':bool(frame.index.has_duplicates),'monotonic':bool(frame.index.is_monotonic_increasing)}
finally:c.close_connection()
# Accounts never included in this report; scrub any incidental broker error text.
import re
s=re.sub(r'\b[UD][A-Z]*[0-9]+\b','[account redacted]',json.dumps(out,indent=2,default=str))
(DATA/(Path(__file__).stem+'.json')).write_text(s);print(s)
