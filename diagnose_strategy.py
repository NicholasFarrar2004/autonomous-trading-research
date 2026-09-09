"""Seven predeclared opened-sample diagnostics; never candidate selection."""
import argparse, hashlib, json, logging
from pathlib import Path
import numpy as np
import pandas as pd
from evaluate_strategy import ResearchData, load_reference, account
from sysdata.config.configdata import Config
from systems.provided.example.simplesystem import simplesystem


def system_for(a,m,rule=None):
    cfg=Config('systems.provided.example.simplesystemconfig.yaml')
    cfg.notional_trading_capital=50000;cfg.percentage_vol_target=10;cfg.base_currency='USD'
    cfg.instrument_weights={'SP500_micro':1.0}
    cfg.instrument_div_multiplier=cfg.forecast_div_multiplier=1.0
    if rule:cfg.forecast_weights={'ewmac8':float(rule=='fast'),'ewmac32':float(rule=='slow')}
    return simplesystem(data=ResearchData(a,m.PRICE),config=cfg)


def scalar_cashflows(price,target,rolls,side=2.5,monthly=25,delay=2):
    """Independent scalar cash-flow oracle, no vectorized position/P&L formula."""
    position=0.;last_price=None;last_date=None;rows=[]
    for i,(day,close) in enumerate(price.items()):
        gain=0 if last_price is None else position*(close-last_price)*5
        new=float(target.iloc[i-delay]) if i>=delay else 0.
        trade=abs(new-position)
        rolling=2*abs(position) if bool(rolls.loc[day]) else 0
        if i==len(price)-1:trade+=abs(new)
        days=1 if last_date is None else (day-last_date).days
        cost=(trade+rolling)*side+days*12/365.25*monthly
        rows.append((gain,gain-cost));position=new;last_price=close;last_date=day
    return pd.DataFrame(rows,index=price.index,columns=['gross','net'])


def run(upstream,out):
    logging.disable(logging.CRITICAL)
    a,m,r,audit=load_reference(upstream);s=system_for(a,m)
    raw=s.portfolio.get_notional_position('SP500_micro').reindex(a.index)
    buffer=s.accounts.get_buffered_position('SP500_micro').reindex(a.index)
    fast=system_for(a,m,'fast').portfolio.get_notional_position('SP500_micro').reindex(a.index)
    slow=system_for(a,m,'slow').portfolio.get_notional_position('SP500_micro').reindex(a.index)
    variants={'baseline':raw.round().clip(-1,1),'fractional_capped':raw.clip(-1,1),
              'fractional_uncapped':raw,'rounded_uncapped':raw.round(),
              'fast_only':fast.round().clip(-1,1),'slow_only':slow.round().clip(-1,1),
              'native_buffer_then_cap':buffer.clip(-1,1)}
    rows=[];p=a.loc['2022-01-01':];rolls=r.reindex(p.index)
    for name,t in variants.items():
        t=t.copy();t.iloc[:200]=0
        t=t.reindex(p.index)
        if not np.isfinite(t).all():raise ValueError('Incomplete target '+name)
        summary,daily=account(p,t,rolls)
        summary['position_changes_while_exposed']=summary.pop('completed_rule_episodes')
        q=daily.target_at_close;prior=q.shift().fillna(0)
        summary['completed_directional_episodes']=int(((prior!=0)&(np.sign(q)!=np.sign(prior))).sum())
        summary.update(diagnostic=name,executable_candidate=False,
                       mean_abs_target=float(t.abs().mean()),max_abs_target=float(t.abs().max()))
        rows.append(summary)
        if name=='baseline':
            oracle=scalar_cashflows(p,t,rolls)
            np.testing.assert_allclose(oracle.gross,daily.gross_proxy,rtol=0,atol=1e-9)
            np.testing.assert_allclose(oracle.net,daily.modeled_net,rtol=0,atol=1e-9)
            prior=daily.target_at_close.shift().fillna(0)
            attribution={'gross_long_usd':float(daily.gross_proxy[prior>0].sum()),
                         'gross_short_usd':float(daily.gross_proxy[prior<0].sum()),
                         'by_year':daily[['gross_proxy','modeled_net']].groupby(daily.index.year).sum().to_dict('index')}
            episodes=[];length=0;old=0
            for value in daily.target_at_close:
                if value!=old:
                    if old:episodes.append(length)
                    length=0
                if value:length+=1
                old=value
            attribution['completed_episode_sessions']=episodes
            attribution['terminal_open_episode_sessions']=length if old else 0
    original=raw.reindex(p.index)
    result={'diagnostic_plan_sha256':hashlib.sha256(Path(__file__).with_name('DIAGNOSTIC_PLAN.md').read_bytes()).hexdigest(),
            'trial_count':7,'sample_status':'already-opened exploratory attribution; no holdout or selected winner',
            'independent_scalar_oracle':'every daily gross and net value matched baseline at1e-9USD tolerance',
            'mechanics':{'rounded_to_zero_percent':float((original.abs()<.5).mean()*100),
                        'fractional_over_one_percent':float((original.abs()>1).mean()*100),
                        'rounding_cap_changes_integer_target_percent':float((original.round().abs()>1).mean()*100),
                        'raw_abs_target_median':float(original.abs().median()),
                        'raw_abs_target_max':float(original.abs().max()),
                        'fast_slow_target_sign_disagreement_percent':float((np.sign(fast.reindex(p.index))!=np.sign(slow.reindex(p.index))).mean()*100)},
            'attribution':attribution,'results':rows,'old_baseline_changed':False}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2,allow_nan=False))
    print(json.dumps(result,indent=2));return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--upstream',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();run(a.upstream,a.out)
