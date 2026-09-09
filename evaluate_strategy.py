"""Frozen native EWMAC price-series proxy; no broker imports or writes."""
import argparse, hashlib, json, logging
from pathlib import Path
import numpy as np
import pandas as pd
from native_signal import PaperData
from sysdata.config.configdata import Config
from systems.provided.example.simplesystem import simplesystem

class ResearchData(PaperData):
    def __init__(self, adjusted, denominator):
        super().__init__(pd.DataFrame({'FINAL': adjusted}))
        self.denominator = denominator
    def get_instrument_raw_carry_data(self, code):
        return pd.DataFrame({'PRICE': self.denominator})

def native_targets(adjusted, denominator):
    cfg = Config('systems.provided.example.simplesystemconfig.yaml')
    cfg.notional_trading_capital = 50000
    cfg.percentage_vol_target = 10
    cfg.base_currency = 'USD'
    cfg.instrument_weights = {'SP500_micro': 1.0}
    cfg.instrument_div_multiplier = cfg.forecast_div_multiplier = 1.0
    s = simplesystem(data=ResearchData(adjusted, denominator), config=cfg)
    target = s.portfolio.get_notional_position('SP500_micro').reindex(adjusted.index)
    forecast = s.combForecast.get_combined_forecast('SP500_micro').reindex(adjusted.index)
    bounded = target.round().clip(-1, 1)
    bounded.iloc[:200] = 0
    if not np.isfinite(bounded.iloc[200:]).all():
        raise ValueError('Nonfinite target after warmup')
    return pd.DataFrame({'forecast': forecast, 'uncapped_target': target,
                         'target': bounded.fillna(0).astype(int)})

def account(price, target, rolls, side_cost=2.5, monthly_cost=25, delay=2):
    """Target installed at t+delay close; previous close exposure earns next diff."""
    q = target.shift(delay).fillna(0)
    prior = q.shift().fillna(0)
    gross = prior * price.diff().fillna(0) * 5
    turns = (q-prior).abs()
    roll_sides = rolls.astype(int) * prior.abs() * 2
    # Measurement-boundary liquidation is explicitly separate from rule exits.
    liquidation = abs(float(q.iloc[-1]))
    turns.iloc[-1] += liquidation
    days = price.index.to_series().diff().dt.total_seconds().div(86400).fillna(1)
    infra = days * 12 / 365.25 * monthly_cost
    net = gross-(turns+roll_sides)*side_cost-infra
    equity = 50000+net.cumsum()
    high = equity.cummax().clip(lower=50000)
    completed = int(((prior != 0) & (q != prior)).sum())
    years = max((price.index[-1]-price.index[0]).days+1,1)/365.25
    return {
        'start': str(price.index[0].date()), 'end': str(price.index[-1].date()),
        'observations': len(price), 'calendar_years': years,
        'gross_proxy_usd': float(gross.sum()), 'modeled_net_usd': float(net.sum()),
        'execution_cost_usd': float((turns+roll_sides).sum()*side_cost),
        'infrastructure_scenario_usd': float(infra.sum()),
        'max_drawdown_usd': float((high-equity).max()),
        'simple_annual_return_percent': float(net.sum()/50000/years*100),
        'annualized_daily_vol_percent': float(net.std(ddof=1)/50000*np.sqrt(252)*100),
        'exposed_sessions_percent': float((prior != 0).mean()*100),
        'target_changes': int((q != prior).sum()), 'completed_rule_episodes': completed,
        'boundary_liquidation_sides': liquidation, 'roll_sides': float(roll_sides.sum()),
        'trade_sides_including_boundary': float(turns.sum()),
        'side_cost_usd': side_cost, 'monthly_cost_usd': monthly_cost, 'delay_sessions': delay,
        'actual_total_economic_net': None,
    }, pd.DataFrame({'target_at_close':q,'gross_proxy':gross,'trade_sides':turns,
                      'roll_sides':roll_sides,'modeled_net':net,'equity':equity})

def load_reference(upstream):
    root = upstream/'data/futures'
    paths = {name:root/f'{name}_csv/SP500_micro.csv' for name in ('adjusted_prices','multiple_prices','roll_calendars')}
    raw = {k:pd.read_csv(p,index_col=0,parse_dates=True) for k,p in paths.items()}
    for k in ('adjusted_prices','multiple_prices'):
        f=raw[k]
        if f.index.has_duplicates or not f.index.is_monotonic_increasing:
            raise ValueError('Invalid raw index '+k)
    a=raw['adjusted_prices'].loc['2019-05-06':].iloc[:,0].resample('B').last().dropna()
    m=raw['multiple_prices'].loc['2019-05-06':].resample('B').last().reindex(a.index)
    if not np.isfinite(a).all() or not np.isfinite(m.PRICE).all() or (m.PRICE <= 0).any():
        raise ValueError('Missing or invalid aligned price')
    if a.index.to_series().diff().max().days > 5:
        raise ValueError('Excessive reference data gap')
    rolls=m.PRICE_CONTRACT.ne(m.PRICE_CONTRACT.shift());rolls.iloc[0]=False
    audit={'source':'pinned upstream stale bundled CSV; independent contract provenance unverified',
           'files':{k:{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                       'rows':len(raw[k]),'first':str(raw[k].index[0]),'last':str(raw[k].index[-1])} for k,p in paths.items()},
           'post_launch_daily_rows':len(a),'observed_contract_changes':int(rolls.sum()),
           'pre_launch_rows_excluded':int((raw['adjusted_prices'].index<pd.Timestamp('2019-05-06')).sum()),
           'max_absolute_raw_vs_adjusted_diff':float((m.PRICE.diff()-a.diff()).abs().max()),
           'tradable_backtest_ready':False,
           'limitations':['MES-labelled data predates product launch','post-launch price provenance not independently verified',
                          'adjusted prices and historical roll selection are not point-in-time tradable fills',
                          'stale since March2024; no current forward evidence','no actual commission/shared project cost ledger']}
    return a,m,rolls,audit

def run(upstream,out):
    logging.disable(logging.CRITICAL)
    a,m,rolls,audit=load_reference(upstream)
    targets=native_targets(a,m.PRICE)
    # Fixed prefix checks before evaluating returns; never used for parameter tuning.
    for n in (250,500,800):
        prefix=native_targets(a.iloc[:n],m.PRICE.iloc[:n])
        np.testing.assert_allclose(prefix.uncapped_target.iloc[200:],targets.uncapped_target.iloc[200:n],rtol=1e-10,atol=1e-10)
    out.mkdir(parents=True,exist_ok=True)
    targets.to_csv(out/'native-targets.csv')
    summaries=[]
    partitions={'development':(a.index[200],'2021-12-31'),'frozen_evaluation':('2022-01-01',a.index[-1]),'all_post_warmup':(a.index[200],a.index[-1])}
    for part,(start,end) in partitions.items():
        p=a.loc[start:end];r=rolls.reindex(p.index)
        # Each partition begins flat, after partition-local execution lag.
        t=targets.target.reindex(p.index)
        for side in (1.5,2.5,5.0):
            for monthly in (0,25,100):
                for name,signal in [('ewmac',t),('long_one',pd.Series(1,index=p.index)),('cash',pd.Series(0,index=p.index))]:
                    v,d=account(p,signal,r,side,monthly if name!='cash' else 0)
                    v.update(partition=part,strategy=name);summaries.append(v)
                    if side==2.5 and monthly==25:d.to_csv(out/f'{part}-{name}-daily.csv')
        v,_=account(p,t,r,2.5,25,delay=3);v.update(partition=part,strategy='ewmac_delay3');summaries.append(v)
    result={'protocol_sha256':hashlib.sha256(Path(__file__).with_name('VALIDATION_PROTOCOL.md').read_bytes()).hexdigest(),
            'audit':audit,'prefix_invariance_checks':[250,500,800],
            'interpretation':'Exploratory price-series proxy only; not a verified tradable backtest or proof of profitability.',
            'results':summaries}
    (out/'evaluation.json').write_text(json.dumps(result,indent=2,allow_nan=False))
    # Public result contains summary statistics/hashes only, no licensed price series.
    print(json.dumps({'audit':audit,'base':[x for x in summaries if x['side_cost_usd']==2.5 and x['monthly_cost_usd'] in (25,) and x['partition']=='frozen_evaluation']},indent=2))
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--upstream',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();run(args.upstream,args.out)
