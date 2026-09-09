"""Dependency-free evidence walkthrough. Does not model, connect, or trade."""
import json
from pathlib import Path
r=json.loads(Path(__file__).with_name('paper-evidence.json').read_text())
gross=(r['cleanup_fill']-r['entry_fill'])*r['quantity']*r['multiplier']
assert gross==r['gross_simulated_pnl_usd']
assert r['final_position']==r['final_open_orders']==r['restart_new_orders']==0
assert r['net_simulated_pnl_usd'] is None and not r['profitability_evidence']
print('Saved paper evidence: signal -> entry -> reconnect (+1) -> cleanup -> flat')
print('Gross simulated P&L: USD %.2f; fees and net P&L: unknown.'%gross)
print('Restart: zero new orders. This walkthrough makes no broker connection.')
