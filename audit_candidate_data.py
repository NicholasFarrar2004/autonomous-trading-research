"""Pinned public data-source audit and fail-closed diversified reference gate.

Downloads price files privately; computes quality/coverage only, never strategy P&L.
"""
import argparse, hashlib, json, urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
import pandas as pd

SOURCE='bug-or-feature/pst-csv-data'
COMMIT='ef27b05c5d3305834afc4579cef6d8945b6801eb'
INSTRUMENTS=('SOFR','US10','CORN','SP500')


def inspect_csv(path,asof):
    f=pd.read_csv(path,index_col=0,parse_dates=True)
    if not isinstance(f.index,pd.DatetimeIndex) or f.empty:raise ValueError('No dated data')
    daily=f.resample('B').last()
    primary='PRICE' if 'PRICE' in f.columns else f.columns[0]
    valid=daily[primary].dropna()
    numeric=f.select_dtypes(include='number')
    summary={'rows':len(f),'daily_valid_prices':len(valid),'first':str(f.index.min()),'last':str(f.index.max()),
             'age_calendar_days':(asof-f.index.max().date()).days,
             'duplicate_timestamps':int(f.index.duplicated().sum()),
             'ordered':bool(f.index.is_monotonic_increasing),
             'missing_primary_rows':int(f[primary].isna().sum()),
             'infinite_numeric_cells':int(np.isinf(numeric.to_numpy()).sum()),
             'max_valid_date_gap_days':int(valid.index.to_series().diff().dt.days.max()),
             'columns':list(f.columns),'sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest()}
    if 'PRICE_CONTRACT' in f:
        summary['missing_contract_rows']=int(f.PRICE_CONTRACT.isna().sum())
        summary['forward_and_contract_columns_present']=all(x in f for x in ('FORWARD','FORWARD_CONTRACT'))
    return summary


def gate(summaries,exact_paths,fx_present,provenance_verified):
    reasons=[]
    for instrument in INSTRUMENTS:
        for kind in ('adjusted_prices','multiple_prices'):
            key=f'data/{kind}_csv/{instrument}.csv'
            if key not in exact_paths:reasons.append('Missing exact mapping: '+key)
            elif key not in summaries:reasons.append('Required price file not audited: '+key)
    if not fx_present:reasons.append('Missing required USDGBP FX series for native GBP-base reference')
    if not provenance_verified:reasons.append('Point-in-time individual-contract and roll/source provenance unverified')
    for name,x in summaries.items():
        if not 0 <= x['age_calendar_days'] <= 7:reasons.append('Stale beyond7-day gate: '+name)
        if x['duplicate_timestamps'] or not x['ordered'] or x['missing_primary_rows'] or x['infinite_numeric_cells'] or x['max_valid_date_gap_days']>5:
            reasons.append('Quality fault or unresolved gap: '+name)
    freshness=[r for r in reasons if r.startswith('Stale beyond')]
    historical=[r for r in reasons if not r.startswith('Stale beyond')]
    return {'passed':not reasons,'reasons':reasons,'performance_calculated':False,
            'historical_gate':{'passed':not historical,'reasons':historical},
            'forward_freshness_gate':{'passed':not freshness,'reasons':freshness}}



def check_equity_mapping(upstream):
    root=upstream/'data/futures'
    a=pd.read_csv(root/'multiple_prices_csv/SP500.csv',index_col=0,parse_dates=True).loc['2019-05-06':]
    b=pd.read_csv(root/'multiple_prices_csv/SP500_micro.csv',index_col=0,parse_dates=True).loc['2019-05-06':]
    x=a[['PRICE','PRICE_CONTRACT']].join(b[['PRICE','PRICE_CONTRACT']],lsuffix='_standard',rsuffix='_micro',how='inner').dropna()
    cfg=pd.read_csv(root/'csvconfig/instrumentconfig.csv')
    size=cfg[cfg.Instrument.isin(['SP500','SP500_micro'])][['Instrument','Pointsize','Currency']].to_dict('records')
    return {'source':'original pinned upstream bundled multiple-price files, postMES launch overlap only',
            'aligned_valid_rows':len(x),'equal_price_rows':int((x.PRICE_standard==x.PRICE_micro).sum()),
            'equal_contract_label_rows':int((x.PRICE_CONTRACT_standard==x.PRICE_CONTRACT_micro).sum()),
            'instrument_metadata':size,
            'conclusion':'Bundled price/contract overlap and native point sizes are checked. This does not authenticate the separate community provider or actual micro/full-size fills; automatic source substitution remains blocked.'}


def run(out,upstream):
    out.mkdir(parents=True,exist_ok=True)
    headers={'User-Agent':'Frozen research data quality audit'}
    url=f'https://api.github.com/repos/{SOURCE}/git/trees/{COMMIT}?recursive=1'
    tree=json.load(urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=30))
    paths={x['path'] for x in tree['tree'] if x['type']=='blob'}
    # Audit micro-labelled series as a mapping diagnostic; never silently map it to SP500.
    selected=sorted(p for p in paths if p.endswith('.csv') and p.split('/')[-1] in ('SOFR.csv','US10.csv','CORN.csv','SP500_micro.csv'))
    if len(selected)!=8:raise ValueError('Pinned expected file set differs')
    asof=datetime.now(timezone.utc).date()
    def fetch(path):
        data=urllib.request.urlopen(urllib.request.Request(f'https://raw.githubusercontent.com/{SOURCE}/{COMMIT}/{path}',headers=headers),timeout=45).read()
        dest=out/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
        return path,inspect_csv(dest,asof)
    with ThreadPoolExecutor(max_workers=4) as pool:summaries=dict(pool.map(fetch,selected))
    config=upstream/'systems/provided/example/simplesystemconfig.yaml'
    result={'source':SOURCE,'commit':COMMIT,'retrieved_at':datetime.now(timezone.utc).isoformat(),
            'registered_native_config_sha256':hashlib.sha256(config.read_bytes()).hexdigest(),
            'bounded_mapping_check':check_equity_mapping(upstream),
            'files':summaries,'gate':gate(summaries,paths,any('USDGBP' in p for p in paths),False),
            'new_data_is_not_certified_unseen':True,'prices_published':False}
    (out/'candidate-data-audit.json').write_text(json.dumps(result,indent=2,allow_nan=False))
    print(json.dumps(result,indent=2));return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);p.add_argument('--upstream',type=Path,required=True)
    a=p.parse_args();run(a.out,a.upstream)
