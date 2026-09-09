# Frozen strategy evaluation protocol v1

Frozen 2026-09-09 before calculating strategy returns. Existing authorization to continue historical evaluation, paper workflows and sanitized publication covers this phase. No real capital, account changes, paid services or indefinite process.

## Problem and success

The eleven previous forced paper round trips tested execution, not strategy returns. Evaluate the existing native example without optimizing it. Success for this phase means reproducible, chronologically delayed decisions, explicit costs and benchmarks, disclosed data gaps, and fail-closed recovery. A positive exploratory result is insufficient for capital deployment. Reject economic readiness whenever costs/provenance are unresolved, net is negative under a stated scenario, or genuine forward evidence is absent. No user loss tolerance or live risk budget is inferred.

## Frozen rules

Pinned pysystemtrade simplesystem; EWMAC 8/32 and 32/128, forecast scalars 5.3 and 2.65, equal weights, forecast and instrument diversification multipliers 1. Native volatility/forecast cap defaults remain pinned. USD50,000 fixed simulated capital, 10% annual volatility target, USD base, MES multiplier5, nearest-even integer rounding with absolute target capped at1. No compounding, carry rule, optimization, stop-loss overlay, or discretionary entry. Close when target becomes0; reversal closes then opens the opposite side. Otherwise retain position. These test assumptions are not recommended capital/risk settings.

At least200 observed daily prices warm up the native stages. Decision uses a completed date t; historical target is installed at close of observed session t+2, then earns subsequent price changes. The extra full-session lag avoids pretending settlement was available at the prior session's next open. No backfilled prices or future observations. Forecast recomputation on prefixes must agree with corresponding full-series prefixes.

## Data and chronology

Audit pinned upstream adjusted and multiple-price MES files without publishing their prices. Data before MES launch on2019-05-06 is excluded even for warmup. Bundled MES history extending into1982 is necessarily proxy/backfilled history; post-launch contract provenance also requires independent verification. Upstream explicitly documents bundled files stale since March2024. Use only as exploratory reference, not authenticated tradable-contract or point-in-time evidence.

Development period: after200 warmup observations through2021-12-31. Frozen chronological evaluation: 2022-01-01 through the last available2024 record. Splits are set now; neither optimization nor parameter selection follows evaluation. Public historical data cannot be a truly unseen market holdout. Reserve future post-freeze observations for genuine forward evidence. No claim that one instrument/fewer than five post-launch years proves broad profitability.

Primary exploratory accounting uses adjusted daily price differences at multiplier5. Because adjusted differences cannot prove tradable roll execution, label all resulting P&L as a price-series proxy. Charge an explicit pair of transactions at each observed PRICE_CONTRACT change when exposure is nonzero; this is a cost proxy, not reconstruction of individual contract fills. Report roll counts and raw/adjusted discontinuity diagnostics. Do not mix this result with previous IB normalized continuous-series execution tests.

A valid tradable backtest additionally needs dated individual-contract prices, exchange expiry calendars, a prospective deterministic roll rule, overlap on both roll legs, source/timezone/vintage and executable timing. Without these, record the blocker instead of labeling proxy P&L valid tradable returns. Existing IBKR read-only history is preferred when Gateway is available; no synthetic replacement for missing actual observations.

## Costs, benchmarks and reports

Per-contract-side execution drag scenarios, frozen: low $1.50, base $2.50, stress $5.00. Each includes estimated commission/exchange/regulatory fees plus spread/slippage, not a fill-derived actual fee. Current official IBKR low-volume micro commission is$0.25/side plus exchange/regulatory charges; CME table lists MES$0.35 before applicable additional fees. Report assumptions rather than claiming these are total actual charges. Infrastructure/data/tool cost scenarios: $0,$25,$100 per month, allocated by calendar days/365.25*12. Zero means incremental-cost scenario only, not known total project cost. Exact actual commissions and shared startup/tool allocations remain unknown. No financing/interest credited; USD base; taxes excluded. Report modeled net separately from unknown actual total economic net.

Benchmarks: flat cash with zero assumed interest and continuous long1MES using identical delayed start/end and cost assumptions. Report gross, modeled net, dollar drawdown from starting equity, annualized return/volatility, exposure, target changes, completed directional episodes, open/end liquidation, roll charges and calendar duration. A final liquidation is a measurement-boundary close, not a rule exit. Sensitivity is costs and one extra execution-delay session only; do not choose the best result as a new strategy.

## Forward and recovery scope

Reuse native signals and existing exact-paper-account localhost4002 guard, contract allowlist, maximum1MES exposure and order, expiry>=7days, stale-data and STOP controls. A forward observation may be unchanged or flat. Do not force an entry/exit to create evidence. Journal a decision once per actual completed date and frozen strategy identity. Pending-send intent is committed before network. Restart must reconcile complete broker positions, open orders, completed orders and executions; absent evidence does not prove an ambiguous order was never sent. Unknown/partial/mismatched state blocks new risk. Reversal is two separately reconciled one-contract orders, never an unbounded two-contract order.

No automated writer is deployed until a concrete bounded supervision window, fresh executable quote entitlement, expiry response and observation cadence exist. Prepare a forward decision/recovery workflow with broker writes disabled; do not reuse immediate-cleanup operate.py as a strategy executor. The current one-shot workflow cannot responsibly hold a daily trend position after the supervised session ends. A finite supervised operating plan is the remaining dependency, not permission to launch an indefinite scheduler.
