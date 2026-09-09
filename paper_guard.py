"""Local onboarding guard. No strategy changes; paper observation only."""
from pathlib import Path
import re
from ib_async import IB


class PaperGuardError(RuntimeError):
    pass


def validate_paper_config(config, host, port, account):
    def need(name):
        value = getattr(config, name, None)
        if value is None:
            raise PaperGuardError(f"Missing required paper configuration: {name}")
        return value

    if need('paper_environment') != 'paper-read-only':
        raise PaperGuardError('Only paper-read-only is supported by this build')
    if host != '127.0.0.1' or type(port) is not int or port != 4002:
        raise PaperGuardError('Only local paper Gateway at 127.0.0.1:4002 is allowed')
    allowlist = need('paper_account_allowlist')
    if (not isinstance(account, str) or not re.fullmatch(r'DUT?[0-9]+', account)
            or allowlist != [account] or need('broker_account') != account):
        raise PaperGuardError('Verified paper account must match the single account allowlist')
    # DU/DUT is an extra conservative filter, not proof of paper identity.
    raw_root = Path(need('paper_state_root'))
    root = raw_root.resolve()
    if not raw_root.is_absolute() or root.name != 'paper':
        raise PaperGuardError('An absolute, separate paper state root is required')
    for key, leaf in [('parquet_store', 'parquet'), ('backtest_store_directory', 'backtests'),
                      ('csv_backup_directory', 'csv-backups'), ('mongo_dump_directory', 'mongo-dump'),
                      ('echo_directory', 'echo')]:
        value = Path(need(key))
        if not value.is_absolute() or value.resolve() != root / leaf:
            raise PaperGuardError(f'State path is not isolated: {key}')
    if (need('mongo_db') != 'pysystemtrade_paper' or need('mongo_host') != '127.0.0.1'
            or need('mongo_dump_all') is not False):
        raise PaperGuardError('Separate local paper database and scoped backup required')


def verify_managed_account(ib, account):
    if ib.managedAccounts() != [account]:
        raise PaperGuardError('Connected account set does not match verified paper account')


class ReadOnlyPaperIB(IB):
    """Block native high-level write methods in addition to Gateway read-only.

    Not a security boundary against arbitrary Python or direct low-level clients.
    """
    def _write_blocked(self, *args, **kwargs):
        raise PaperGuardError('Order/account mutation disabled during paper onboarding')

    def placeOrder(self, contract=None, order=None):
        lease = getattr(self, '_bounded_paper_lease', None)
        if lease is None:
            return self._write_blocked()
        lease.validate(self, contract, order)
        return IB.placeOrder(self, contract, order)

    def cancelOrder(self, order=None, *args, **kwargs):
        lease = getattr(self, '_bounded_paper_lease', None)
        if lease is None or order.orderRef not in lease.used_refs:
            return self._write_blocked()
        verify_managed_account(self, lease.account)
        return IB.cancelOrder(self, order, *args, **kwargs)

    reqGlobalCancel = _write_blocked
    exerciseOptions = _write_blocked
    replaceFA = _write_blocked


class BoundedPaperLease:
    """One entry and one reducing exit, IOC limits only, with an expiring entry gate.

    An application safeguard, not protection against arbitrary Python code.
    Caller must persist intent before arming each order and reconcile broker state.
    """
    def __init__(self, account, conid, target, stop_path, lifetime=120):
        import time
        if not re.fullmatch(r'DUT?[0-9]+', account) or type(conid) is not int or conid <= 0:
            raise PaperGuardError('Invalid paper identity/contract')
        if target not in (-1, 1) or not 0 < lifetime <= 120:
            raise PaperGuardError('Invalid one-contract paper scope')
        self.account, self.conid, self.target = account, conid, target
        self.stop_path = Path(stop_path)
        self.deadline = time.monotonic() + lifetime
        self.used_refs = set()
        self.intent = None

    def arm_intent(self, ref, phase, position, limit):
        import math
        if phase not in ('entry', 'cleanup') or not ref.startswith('workos-paper-'):
            raise PaperGuardError('Invalid intent')
        if len(self.used_refs) >= 2 or ref in self.used_refs or not math.isfinite(limit) or limit <= 0:
            raise PaperGuardError('Duplicate intent or invalid limit')
        if (phase == 'entry' and (position != 0 or self.used_refs)) or (phase == 'cleanup' and position != self.target):
            raise PaperGuardError('Position does not permit this intent')
        self.intent = (ref, phase, position, limit)

    def validate(self, ib, contract, order):
        import time
        verify_managed_account(ib, self.account)
        if not ib.isConnected() or ib.client.host != '127.0.0.1' or ib.client.port != 4002:
            raise PaperGuardError('Wrong connection')
        if self.intent is None:
            raise PaperGuardError('No persisted/armed intent')
        ref, phase, position, limit = self.intent
        direction = self.target if phase == 'entry' else -position
        if phase == 'entry' and (time.monotonic() >= self.deadline or self.stop_path.exists()):
            raise PaperGuardError('Expired or stopped entry')
        if (contract.conId != self.conid or contract.secType != 'FUT' or contract.symbol != 'MES'
                or contract.currency != 'USD' or str(contract.multiplier) != '5'):
            raise PaperGuardError('Contract outside lease')
        if (order.account != self.account or order.orderType != 'LMT' or order.totalQuantity != 1
                or order.tif != 'IOC' or order.orderRef != ref or ref in self.used_refs
                or order.action != ('BUY' if direction > 0 else 'SELL') or order.lmtPrice != limit):
            raise PaperGuardError('Order outside lease')
        self.used_refs.add(ref)
        self.intent = None  # consumed before the network call; ambiguous sends cannot retry
