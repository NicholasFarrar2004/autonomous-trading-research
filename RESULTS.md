# Results and limitations

The native paper run bought one MES at 7682.25, reconnected and observed a position of one, then sold it at 7682.00. Both orders reached Filled. Final and independent checks found no nonzero positions and no open orders. An actual repeat process found the saved claim and sent no new entry. Gateway read-only was restored; the runtime STOP marker disabled further entry.

The expanded 28-test packaged suite passed with network access denied. See [the ten-cycle execution-validation milestone](BATCH_RESULTS.md) for the subsequent broker batch and [sanitized batch evidence](batch-evidence.json) for its retained observations. The packaged version replaces private configuration and broker history in tests with synthetic fixtures and isolates test storage. Packaging verification is distinct from the earlier broker test and does not repeat any trade.

## Accounting

Gross simulated fill P&L is (7682.00 - 7682.25) x 5 = -USD 1.25. Broker commission fields had zero values with no currency, so fee data is unavailable rather than zero. Net simulated P&L is unknown.

The full-period measure is ending liquidation equity + withdrawals - contributions - starting equity - external attributable costs not already reflected in equity. Track commissions, exchange/regulatory costs, data, hosting/computer use, tools/LLM subscriptions, startup work, financing and FX where applicable. Record unknowns and allocation methods. Do not double-count fees already in equity or slippage embedded in fills. Keep real project cash costs separate from simulated returns. Taxes require separate treatment.

## Unproven behavior

Delayed quotes are not realistic live execution evidence. IB continuous prices are not the production roll pipeline. Repeated execution of the same daily signal does not demonstrate profitability, safe long-term operation, live permission or adequate capital. Abrupt failure during transmission, process termination with an uncertain pending order, Gateway restart and uncertain cleanup recovery were not tested against the broker. The runner fails closed and requires reconciliation in unresolved states.

The source environment had unavailable live margin/futures access. This is an operational boundary, not a claim about another user's account or a reason to change financial declarations.
