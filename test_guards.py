import copy
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest
from unittest.mock import patch, MagicMock
import yaml
from sysbrokers.IB.paper_guard import PaperGuardError, validate_paper_config, ReadOnlyPaperIB
from sysbrokers.IB.ib_connection import connectionIB

from synthetic_fixture import synthetic_profile
PROFILE = synthetic_profile()

class GuardTests(unittest.TestCase):
    def setUp(self):
        self.cfg = copy.deepcopy(PROFILE)
        # Deliberate local test identifier, not a real account.
        self.cfg.update(broker_account='DU12345678', paper_account_allowlist=['DU12345678'])

    def validate(self, cfg=None, host='127.0.0.1', port=4002, account='DU12345678'):
        validate_paper_config(SimpleNamespace(**(cfg or self.cfg)), host, port, account)

    def test_actual_unconfigured_profile_fails(self):
        with self.assertRaises(PaperGuardError): self.validate(PROFILE,account=None)

    def test_valid_isolated_profile(self): self.validate()

    def test_dut_format_still_requires_exact_allowlist(self):
        cfg=dict(self.cfg,broker_account='DUT12345678',paper_account_allowlist=['DUT12345678'])
        self.validate(cfg,account='DUT12345678')
        cfg['paper_account_allowlist']=['DUT999']
        with self.assertRaises(PaperGuardError): self.validate(cfg,account='DUT12345678')
        for account in ['U12345678','DT12345678','DUTX123','DU','DUT']:
            cfg=dict(self.cfg,broker_account=account,paper_account_allowlist=[account])
            with self.assertRaises(PaperGuardError): self.validate(cfg,account=account)

    def test_live_and_remote_endpoints_fail(self):
        for host,port in [('127.0.0.1',4001),('127.0.0.1',7496),('example.com',4002),('127.0.0.1','4002')]:
            with self.subTest(host=host,port=port),self.assertRaises(PaperGuardError): self.validate(host=host,port=port)

    def test_environment_and_account_fail_closed(self):
        for key,value in [('paper_environment','live'),('paper_environment',None),('paper_account_allowlist',[]),('paper_account_allowlist',['DU999']),('broker_account','U12345678')]:
            cfg=dict(self.cfg);cfg[key]=value
            with self.subTest(key=key,value=value),self.assertRaises(PaperGuardError): self.validate(cfg)
        with self.assertRaises(PaperGuardError):self.validate(account='U12345678')

    def test_state_and_backup_separation(self):
        for key,value in [('mongo_db','production'),('mongo_host','remote'),('mongo_dump_all',True),('parquet_store','/tmp/live/parquet'),('echo_directory','data.echos')]:
            cfg=dict(self.cfg);cfg[key]=value
            with self.subTest(key=key),self.assertRaises(PaperGuardError):self.validate(cfg)

    def test_symlink_cannot_escape_state_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp);(p/'paper').mkdir();(p/'outside').mkdir();(p/'paper'/'parquet').symlink_to(p/'outside',target_is_directory=True)
            cfg=dict(self.cfg);cfg['paper_state_root']=str(p/'paper')
            for key,leaf in [('parquet_store','parquet'),('backtest_store_directory','backtests'),('csv_backup_directory','csv-backups'),('mongo_dump_directory','mongo-dump'),('echo_directory','echo')]:cfg[key]=str(p/'paper'/leaf)
            with self.assertRaises(PaperGuardError):self.validate(cfg)

    def native_connect(self, cfg, accounts, connect_error=None):
        obj=object.__new__(connectionIB)
        broker=MagicMock();broker.managedAccounts.return_value=accounts
        broker.connect.side_effect=connect_error
        with patch('sysbrokers.IB.ib_connection.get_production_config',return_value=SimpleNamespace(**cfg)),patch('sysbrokers.IB.ib_connection.ReadOnlyPaperIB',return_value=broker) as factory,patch('sysbrokers.IB.ib_connection.time.sleep'):
            try:obj._init_connection('127.0.0.1',4002,100,account=cfg.get('broker_account'))
            except BaseException as exc:return obj,broker,factory,exc
        return obj,broker,factory,None

    def test_native_path_blocks_before_constructing_client(self):
        obj,broker,factory,error=self.native_connect(dict(PROFILE,broker_account=None,paper_account_allowlist=[]),[])
        self.assertIsInstance(error,PaperGuardError);factory.assert_not_called();broker.connect.assert_not_called()

    def test_native_path_checks_actual_account_and_disconnects(self):
        for accounts in [[],['U12345678'],['DU12345678','DU999']]:
            with self.subTest(accounts=accounts):
                obj,broker,factory,error=self.native_connect(self.cfg,accounts)
                self.assertIsInstance(error,PaperGuardError);broker.disconnect.assert_called_once();self.assertFalse(hasattr(obj,'_ib'))

    def test_native_connect_error_disconnects(self):
        obj,broker,factory,error=self.native_connect(self.cfg,[],ConnectionError('test connection error'))
        self.assertIsInstance(error,ConnectionError);broker.disconnect.assert_called_once()

    def test_native_path_passes_readonly_and_exposes_only_verified_client(self):
        obj,broker,factory,error=self.native_connect(self.cfg,['DU12345678'])
        self.assertIsNone(error);broker.connect.assert_called_once_with('127.0.0.1',4002,clientId=100,account='DU12345678',readonly=True);self.assertIs(obj.ib,broker)

    def test_native_profile_loader_and_actual_storage_location(self):
        import os
        import pandas as pd
        from sysdata.config.private_config import get_private_config_as_dict
        from sysdata.parquet.parquet_access import ParquetAccess
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);private=base/'private';private.mkdir()
            profile=synthetic_profile(base)
            (private/'private_config.yaml').write_text(yaml.safe_dump(profile))
            with patch.dict(os.environ, {'PYSYS_PRIVATE_CONFIG_DIR':str(private)}):
                loaded=get_private_config_as_dict()
            self.assertEqual(loaded,profile)
            accessor=ParquetAccess(loaded['parquet_store'])
            data=pd.DataFrame({'value':[1.0,2.0]})
            accessor.write_data_given_data_type_and_identifier(data,'preflight_only','location_check')
            pd.testing.assert_frame_equal(data,accessor.read_data_given_data_type_and_identifier('preflight_only','location_check'))

    def test_high_level_write_methods_reject_before_client_access(self):
        obj=object.__new__(ReadOnlyPaperIB)
        for method in ['placeOrder','cancelOrder','reqGlobalCancel','exerciseOptions','replaceFA']:
            with self.subTest(method=method),self.assertRaises(PaperGuardError):getattr(obj,method)()
        # Avoid base-class destructor on this deliberately uninitialized object.
        obj.disconnect=lambda:None

if __name__=='__main__':unittest.main()
