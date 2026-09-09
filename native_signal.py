"""Native example stages on one explicitly selected contract; no broker writes."""
import json,math,logging
from pathlib import Path
from datetime import datetime,timedelta
from zoneinfo import ZoneInfo
import pandas as pd
import numpy as np
from sysdata.sim.sim_data import simData
from sysdata.config.configdata import Config
from systems.provided.example.simplesystem import simplesystem
from project_paths import DATA
ROOT=DATA
class PaperData(simData):
 def __init__(self,frame):self.frame=frame
 def get_instrument_list(self):return ['SP500_micro']
 def get_raw_price(self,code):assert code=='SP500_micro';return self.frame['FINAL']
 def get_value_of_block_price_move(self,code):return 5.0
 def get_instrument_raw_carry_data(self,code):return pd.DataFrame({'PRICE':self.frame.FINAL})
 def get_instrument_currency(self,code):return 'USD'
 def get_fx_for_instrument(self,instrument_code,base_currency):assert base_currency=='USD';return pd.Series(1.0,index=self.frame.index)

def validate_history(f,now=None):
 now=now or datetime.now(ZoneInfo('America/New_York'))
 if len(f)<200:raise ValueError('Fewer than 200 daily bars')
 if f.index.has_duplicates or not f.index.is_monotonic_increasing:raise ValueError('Unordered or duplicate history')
 if not np.isfinite(f.values).all() or (f[['OPEN','HIGH','LOW','FINAL']]<=0).any().any():raise ValueError('Missing/nonpositive price')
 if ((f.HIGH<f[['OPEN','LOW','FINAL']].max(axis=1)) | (f.LOW>f[['OPEN','HIGH','FINAL']].min(axis=1))).any():raise ValueError('Invalid OHLC')
 if (f.VOLUME<0).any() or (f.VOLUME>0).sum()<200:raise ValueError('Insufficient traded history')
 if max(f.index.to_series().diff().dropna()).days>5:raise ValueError('Excessive history gap')
 latest=f.index[-1].date()
 if latest>now.date() or (latest==now.date() and now.hour<18) or (now.date()-latest).days>4:raise ValueError('Unfinished or stale daily data')
 if f.FINAL.diff().tail(35).std()<=0:raise ValueError('No measurable volatility')

def build_signal():
 logging.disable(logging.CRITICAL)
 f=pd.read_parquet(ROOT/'continuous-history.parquet');validate_history(f)
 cfg=Config('systems.provided.example.simplesystemconfig.yaml')
 cfg.notional_trading_capital=50000;cfg.percentage_vol_target=10;cfg.base_currency='USD'
 cfg.instrument_weights={'SP500_micro':1.0};cfg.instrument_div_multiplier=1.0;cfg.forecast_div_multiplier=1.0
 system=simplesystem(data=PaperData(f),config=cfg)
 target=float(system.portfolio.get_notional_position('SP500_micro').iloc[-1])
 forecast=float(system.combForecast.get_combined_forecast('SP500_micro').iloc[-1])
 if not math.isfinite(target+forecast):raise ValueError('Nonfinite native forecast/target')
 bounded=max(-1,min(1,int(round(target))))
 result={'strategy':'native example ewmac8_32 + ewmac32_128 equal weights','simulated_notional':50000,'volatility_target_percent':10,'history_rows':len(f),'data_date':str(f.index[-1].date()),'combined_forecast':forecast,'uncapped_target':target,'bounded_target':bounded,'max_contracts':1,'price':float(f.FINAL.iloc[-1]),'not_live_strategy_reproduction':True}
 (ROOT/'signal.json').write_text(json.dumps(result,indent=2));return result
if __name__=='__main__':print(json.dumps(build_signal(),indent=2))
