import unittest, tempfile
from pathlib import Path
from datetime import date
import numpy as np
import pandas as pd
from diagnose_strategy import scalar_cashflows
from evaluate_strategy import account
from audit_candidate_data import gate, inspect_csv, INSTRUMENTS

class Diagnostics(unittest.TestCase):
    def test_independent_oracle_across_reversals_rolls_and_gaps(self):
        idx=pd.bdate_range('2024-01-01',periods=40).delete([9,21])
        rng=np.random.default_rng(413)
        p=pd.Series(100+np.cumsum(rng.normal(0,2,len(idx))),index=idx)
        t=pd.Series(rng.choice([-1,0,1],len(idx)),index=idx)
        r=pd.Series(False,index=idx);r.iloc[[4,14,28]]=True
        _,actual=account(p,t,r,2.5,25)
        independent=scalar_cashflows(p,t,r)
        np.testing.assert_allclose(actual.gross_proxy,independent.gross,atol=1e-9)
        np.testing.assert_allclose(actual.modeled_net,independent.net,atol=1e-9)
    def test_exact_mapping_fx_provenance_and_freshness_gate(self):
        paths={f'data/{kind}_csv/{i}.csv' for i in INSTRUMENTS for kind in ('adjusted_prices','multiple_prices')}
        good={'age_calendar_days':1,'duplicate_timestamps':0,'ordered':True,'missing_primary_rows':0,'infinite_numeric_cells':0,'max_valid_date_gap_days':4}
        complete={p:good for p in paths}
        self.assertTrue(gate(complete,paths,True,True)['passed'])
        self.assertFalse(gate({'fixture':good},paths,True,True)['passed'])
        stale={p:{**good,'age_calendar_days':8} for p in paths}
        split=gate(stale,paths,True,True)
        self.assertTrue(split['historical_gate']['passed'])
        self.assertFalse(split['forward_freshness_gate']['passed'])
        for summaries,p,fx,provenance in [(complete,paths-{'data/adjusted_prices_csv/SP500.csv'},True,True),(complete,paths,False,True),(complete,paths,True,False),({p:{**good,'age_calendar_days':8} for p in paths},paths,True,True)]:
            self.assertFalse(gate(summaries,p,fx,provenance)['passed'])
    def test_data_audit_exposes_missing_duplicate_and_stale_values(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'fixture.csv'
            p.write_text('date,price\n2024-01-01,100\n2024-01-02,\n2024-01-02,102\n2024-01-03,103\n')
            a=inspect_csv(p,date(2024,2,1))
            self.assertEqual(a['duplicate_timestamps'],1)
            self.assertEqual(a['missing_primary_rows'],1)
            self.assertEqual(a['age_calendar_days'],29)

if __name__=='__main__':unittest.main()
