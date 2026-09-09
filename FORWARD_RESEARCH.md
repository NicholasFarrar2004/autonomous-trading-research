# Forward research status

The frozen candidate failed the exploratory economic screen. Keep broker writes disabled. The new workflow records actual available observations and previews genuine target changes; it does not call the forced-round-trip executor.

`forward_plan.py` reuses the pinned native EWMAC stages, normalizes IB daily close-time labels to session dates, rejects stale/unfinished/short data, applies the frozen delay and writes one immutable observation per date. Same-date identical reruns are duplicates; changed observations halt for review. This is a shadow workflow, not a paper trading executor. The first record used the existing September8 cache, with a delayed September3 signal and target+1. It is not a new market observation, entry or performance result.

`ForwardJournal` is a separately tested future-executor component. It persists pending intent before any potential network submission and blocks all later intents while unresolved. Reconciliation requires complete fresh evidence, matching position and execution quantities. Duplicate execution IDs are counted once. Missing, conflicting, partial, open or stale evidence cannot cause an automatic retry. These offline tests do not prove actual broker disconnect/partial-fill behavior. It is not wired into an active order sender.

`plan_transition` preserves HOLD and FLAT. A changed signal first closes existing exposure and requires a fresh reconciliation before any opposite entry. It never emits a two-contract reversal. STOP, missing fresh quote or expiry proximity blocks entry; existing exposure inside the expiry guard raises recovery attention. Plans do not send orders. The existing exact-account/endpoint/order lease safeguards remain unchanged.

## Current operating boundary

A bounded read-only probe on September9 found no Gateway listener at localhost4002. Current positions/orders therefore were not freshly verified. The previously saved STOP marker remains present; no lease, broker order, scheduler or background trading service was started. The earlier flat/read-only result is historical, not a current broker snapshot. Restoring connectivity is not a reason to trade this failed candidate.

The existing IB feed was delayed, and its normalized continuous history lacks a verified tradable roll construction. Keep these observations separate from the upstream historical proxy. Neither data source supplies a clean historical-to-forward reproduction by itself.

## Concrete next research session

1. Keep STOP and Gateway read-only on. Start/login to the existing Paper Gateway, confirm the exact private paper identity and localhost4002, then run `capture_paper_state.py`. No new account or data purchase.
2. In a supervised session, retrieve fresh completed daily history and dated individual MES contract metadata using the existing native read-only adapter. Archive immutable data vintages, timezone, receipt time, actual expiry and both legs at each prospective roll. Reject missing overlap and provisional bars.
3. Once daily after the required final settlement is actually available, manually run the shadow recorder. Plan a finite20-trading-session observation period, no order sender or autonomous scheduler. Cached repeats add no observations. Record changes only from actual new sessions; no accelerated fake time.
4. Before interpreting historical/forward comparability, specify and verify an executable timestamp with matching historical quote/bar coverage. The current daily settlement proxy is not an executable close. Roll must use a prospective contract calendar and costs for both legs.
5. Review the20-session shadow log for data/decision/recovery consistency. Twenty sessions do not establish profitability. Do not enable orders for the rejected candidate. A new candidate needs a separately versioned hypothesis and fresh evaluation discipline; do not reuse the opened evaluation period as an untouched holdout.

The required next user action for live read-only observations is a working authenticated Paper Gateway. No user decision blocks the completed offline evaluation or publication. No holding-period position is left open by this work.
