# Project specification

## Problem

Open trading software and positive operator reports do not establish a reproducible profitable deployment. The project needs to separate useful code, credible performance evidence, and operational readiness.

## Success criteria

- Keep live results, paper simulation, synthetic replay and historical backtests separate.
- Reproduce an existing offline scenario, preserve failures, and test corrections without changing the strategy.
- Exercise native signal, sizing, paper order, reconnect and position reconciliation in a finite run.
- Prevent duplicate entry, cap exposure, preserve durable intent, and return to a verified flat state.
- Evaluate eventual full-period economic results after all attributable costs, including unknown costs explicitly.

## Scope

Research ledger and reuse shortlist; pinned Passivbot offline harness correction; native pysystemtrade EWMAC example; bounded IBKR paper coordinator; safety tests; sanitized evidence and reproducible packaging.

## Constraints

No real-money operation, funding or paid data purchase is part of this repository. Prefer upstream components. Use an exact paper account allowlist and local paper endpoint. Keep private configuration and generated data outside the checkout. Stop rather than silently relax failed data gates or retry an ambiguous order.

The paper settings of USD 50,000 simulated notional, a 10% annual volatility target and a maximum of one MES contract were operational-test choices. They are not funding or portfolio recommendations.

## Completed plan

1. Review public evidence and select reusable components.
2. Reproduce offline behavior and correct an isolated terminal-fill harness defect.
3. Verify native paper connection and data compatibility.
4. Run a finite paper round trip, reconnect, reconcile, test duplicate restart, and restore safe defaults.
5. Package code, pins, tests and sanitized documentation for reproducibility.

## Open questions

Production adjusted and multiple-contract histories; longer out-of-sample and forward evaluation; realistic execution costs; attributable operating costs; abrupt order-transmission and Gateway-restart recovery; live eligibility and appropriate future scope. None is resolved by the single paper exercise.


## Expanded execution-test scope

A later authorized phase makes the sanitized repository public and runs up to ten additional paper round trips, at most twenty fills, with unchanged strategy/data/risk limits. Distinct batch/cycle identities preserve the original claim and support duplicate verification after every cycle. Record actual attempts, fills, cancellations, errors, reconnect positions and final state. Do not force fills or treat repeated signal execution as independent strategy evidence. Restore STOP and Gateway read-only after the finite batch.
