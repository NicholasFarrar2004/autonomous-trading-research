# Execution-validation milestone

On September 8, 2026 (EDT), the automated trading pipeline completed ten additional IBKR paper round trips, with twenty filled orders. Ten fresh-process duplicate checks submitted no new orders. Every cycle reconnected to confirm the entry position, then closed it and verified a flat account with no open orders.

The batch ran from 2026-09-09T01:40:19.508972+00:00 to 2026-09-09T01:47:41.486674+00:00 UTC. It extends the earlier single-cycle validation; combined, those records contain eleven round trips and twenty-two fills. The table below covers only the new batch.

## Observed results

| Cycle | Buy fill | Sell fill | Gross simulated P&L (USD) |
|---|---:|---:|---:|
| 1 | 7686.25 | 7686.00 | -1.25 |
| 2 | 7686.00 | 7685.50 | -2.50 |
| 3 | 7685.00 | 7684.75 | -1.25 |
| 4 | 7684.75 | 7684.75 | 0.00 |
| 5 | 7685.25 | 7685.00 | -1.25 |
| 6 | 7685.25 | 7685.00 | -1.25 |
| 7 | 7685.00 | 7685.00 | 0.00 |
| 8 | 7686.50 | 7686.25 | -1.25 |
| 9 | 7687.00 | 7686.75 | -1.25 |
| 10 | 7686.75 | 7686.00 | -3.75 |
| **Total** | | | **-13.75** |

All twenty orders reached Filled; none were rejected or left unfilled. Gross fill P&L uses the MES USD 5 multiplier. Commission fields had zero values without a currency, so fees are unavailable and net P&L is unknown. The earlier round trip was -USD 1.25 gross, making the combined gross result -USD 15.00. Real project costs remain separate and unallocated.

## Methodology

The batch executed the actual paper coordinator in twenty separate processes: ten cycles and ten exact-cycle reruns. Each cycle used a durable unique journal identity, while its rerun reused that identity. The original one-shot identity remains unchanged. The runner stops after ten requested cycles and halts on ambiguous state, non-flat exit, abnormal order status or unexpected broker error.

Native pysystemtrade EWMAC rules (8/32 and 32/128, equally weighted) calculated a combined forecast of 6.758358 from 251 daily continuous-futures observations through September 8. USD 50,000 simulated notional and a 10% volatility target produced an uncapped target of 0.796989 MES contracts, bounded to one contract. These are mechanical validation settings, not a capital recommendation.

Each cycle bought one MES September 2026 contract through an IOC limit order, disconnected and reconnected to confirm +1, then sent a reducing sell and verified zero positions and open orders. Limits used delayed bid/ask quotes with a 20-point price allowance and a maximum accepted spread of two points. A wide allowance prioritizes exercising the paper lifecycle and does not demonstrate competitive execution. Existing account, localhost port 4002, contract-expiry, data-quality, exposure and lease guards remained active.

## Validation and shutdown

The expanded packaged suite passed 28 tests under macOS network denial. Seven batch tests cover bounds and cycle identity, durable claims, invalid/duplicate state, broker errors, unfilled outcomes, STOP handling and no-execution planning. The ten broker duplicate checks and ten entry reconnections add observed integration evidence beyond those offline tests.

After the batch, STOP was recreated. Gateway Read-Only API was enabled, saved and confirmed after reopening settings. A separate API client at 01:48:11 UTC observed zero nonzero positions and zero open orders, verified the exact configured paper account and confirmed the default write guard blocked before the broker. No scheduler is running.

## What these findings establish

This milestone validates repeated native signal-to-order execution, journal isolation, reconnect position checks, reducing cleanup and restart duplicate prevention along the exercised path. It is one daily signal replayed across ten execution cycles, so the cycles are not independent strategy opportunities. Delayed paper fills cannot establish live liquidity, slippage, profitability or production readiness. Uncertain in-flight process failure, Gateway restart and prolonged unattended recovery remain unproven. The negative gross outcome and unknown fees are retained without inferring a strategy return.

[Sanitized machine-readable evidence](batch-evidence.json) preserves the observed fields. Raw account identifiers, execution identifiers, order references, credentials, journal files and broker history remain excluded. [Reproduction](REPRODUCE.md), [operations](OPERATIONS.md) and [cost accounting](RESULTS.md) describe the surrounding workflow.
