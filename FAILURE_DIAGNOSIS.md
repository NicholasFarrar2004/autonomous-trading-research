# Why the first configuration failed, and what to research next

The original loss is reproducible. The strongest next research direction is **data and capital feasibility for the native multiasset reference**, not faster experimentation on the same MES sample. No tested diagnostic supplies a positive base-case replacement. The failed configuration and its report are preserved.

This phase completed seven registered diagnostic calculations, an independent accounting reconstruction, and a real audit of eight free replacement data files. The proposed diversified reference failed its data gate, so no new portfolio performance was calculated.

## What the evidence says

**The result is not explained by an accounting error found here.** An independent scalar session loop reproduced every baseline daily gross and modeled-net value over 562 observations to within 1e-9 USD, including the lag, roll-cost proxy, weekend infrastructure allocation and terminal liquidation. A separate synthetic path exercised reversals and gaps. This does not validate the source's historical rolls or tradable settlement prices.

**Rounding and the cap materially change the intended risk sizing.** The native target had median absolute size 0.72 MES and maximum 4.07. Rounding put 35.2% of targets at zero; the one-contract cap changed the rounded target on 23.7% of dates. The cap was an engineering constraint, not a discovered broker capital requirement. Raising capital while retaining the same cap would not restore the native risk profile. These observations are not permission to raise exposure.

**Costs were not the main source of this loss.** The baseline gross loss was $3,935; base execution/roll charges added $115 and infrastructure allocation $670. Gross P&L from short exposure was−$3,792.50 and from long exposure−$142.50. This describes this sample; it does not justify deleting shorts. Gross results by year were 2022 −$5,460,2023 −$622.50, and 2024 through March+$2,147.50. The partial 2024 rebound does not erase the earlier drawdown.

**Slowing down and buffering do not repair the result in this diagnostic.** Fast/slow raw target signs disagreed on 30.2% of dates. The combined forecast, clipping and integer rounding are nonlinear, so the combined bounded strategy is not the average of two independently rounded strategies. Native buffering reduced changes from 35 to 29 and execution costs from $115 to $100, but modeled net remained −$4,626. Slower-only reduced changes to 15 but still lost $2,718. The 17 completed baseline directional episodes had median 14 sessions, with a 90-session open episode at the measurement boundary. This was not thousands of tiny churn trades.

## All seven registered diagnostic outputs

Opened 2022-01-03 through2024-03-28 sample; delay 2; $2.50 per contract side and $25/month. Amounts USD. Fractional positions cannot be traded as futures, and uncapped variants exceed this project's authorized paper limit. Their costs scale fractionally as a theoretical attribution, not a broker quotation. They are not executable candidates or a new holdout.

| Diagnostic | Gross proxy | Modeled net | Max drawdown | Maximum target contracts |
|---|---:|---:|---:|---:|
| baseline | -3,935 | -4,720 | 8,058 | 1.00 |
| fractional capped | -2,922 | -3,707 | 6,960 | 1.00 |
| fractional uncapped | 544 | -328 | 8,012 | 4.07 |
| rounded uncapped | -481 | -1,341 | 9,003 | 4.00 |
| fast only | 178 | -623 | 5,925 | 1.00 |
| slow only | -1,978 | -2,718 | 6,626 | 1.00 |
| native buffer then cap | -3,856 | -4,626 | 7,924 | 1.00 |

Every base-case diagnostic remains negative. Removing cap/rounding changes exposure and simulated risk, so its improved dollar result is not proof of an improved risk-adjusted strategy. No winner was selected. The diagnostic trial count is seven, including the baseline; two native horizon variants and native buffering were specified before calculating them. [Registration](DIAGNOSTIC_PLAN.md) was committed locally as 40eb19e before these results. The original frozen evaluation was not changed.

## Native strategy fidelity matters

The reused EWMAC stages are native; our portfolio and execution constraints were not the full native example. The pinned example allocates SOFR 40%, US10 10%, CORN 30%, SP500 20%, with GBP 500,000 reference capital, 25% volatility target, forecast diversification 1.1 and instrument diversification 1.5. Our failed variant uses one equity future, USD 50,000,10% volatility and multipliers 1. Native account buffering (forecast buffer 0.10, trade-to-edge enabled) was also omitted from the original mechanics variant. This is a different portfolio, not a reproduction of a manager's historical returns.

The native position-sizing default uses a 35-day estimator mixed with a slower volatility component; the example EWMAC rule calculates its own robust price volatility. Both were reused, not replaced by a simple ad hoc percentage rule. A 10% target is a sizing input, not a promise: the cap/rounding and concentrated exposure produced about 5.96% annualized realized daily volatility in the baseline. Long 1 MES realized 7.70% and was exposed 99.5% of sessions versus 64.2% for the strategy. It is a useful transparent benchmark, but not risk matched.

Carver's own instrument-selection discussion stresses diversification, contract granularity, liquidity and cost rather than selecting markets by their historical pre-cost Sharpe. AQR's paper studies 67 markets across four asset classes with monthly 1/3/12-month signals, not this two-rule daily MES experiment. Its cost estimates explicitly omit some potential roll costs. Those sources motivate a hypothesis and scrutiny, not a promised return or directly transferable cost model.

## Three hypotheses, one recommendation

| Hypothesis | Why it is worth considering | Main barrier / decision |
|---|---|---|
| **H1: native multiasset reference feasibility** | Restores meaningful rates/agriculture/equity exposure before changing signals | Recommended research direction; exact data, roll/FX costs, contract granularity, capital and permissions are not established. SOFR and US10 are related rate markets, not two independent asset classes. |
| H2: slower or buffered single MES | Could reduce rounding threshold changes | Diagnostics already show it does not produce positive base net here; not selected. Requires a new hypothesis and fresh evaluation before further testing. |
| H3: unlevered diversified ETF allocation with separate trend rules | Whole/fractional share granularity could suit a smaller account | Entirely different strategy, data and execution access. Needs dividend-adjusted total returns and its own protocol; no futures performance transfers. Not implemented or selected. |

The GBP 500,000 native setting is a reference simulation assumption, not a recommendation to fund that amount. We have not established a personal deployable capital budget or current margin requirements for that universe. Four correlated equity micro contracts would not substitute for cross-asset diversification. No broker/account switch is proposed as an automatic fix.

## Actual free-data audit: gate failed

The community dataset linked by upstream was retrieved at pinned commit `ef27b05c5d3305834afc4579cef6d8945b6801eb`. All eight audited files ended September 23, 2025, 351 calendar days before this audit. It does add a historical extension beyond the bundled March 2024 snapshot, but is not current forward data or a certified unseen sample.

| Series | Observed daily prices | First raw date | Last raw date | Missing primary raw rows |
|---|---:|---|---|---:|
| CORN | 10,835 | 1982-09-22 | 2025-09-23 | 0 |
| SOFR | 9,127 | 1989-06-21 | 2025-09-23 | 2 |
| SP500_micro | 7,020 | 1997-12-15 | 2025-09-23 | 304 |
| US10 | 10,871 | 1982-08-30 | 2025-09-23 | 739 |

Counts are equal for the paired adjusted/multiple files. Missing raw observations can coexist with valid daily observations and need investigation; they do not prove every daily return is unusable. The longest observed SP500_micro daily gap is six calendar days and requires holiday/source review. The old product labels and pre-launch history also require explicit proxy/splice documentation.

Freshness alone does not invalidate a closed historical study. The audit reports separate historical and forward-freshness gates. Historical mapping, FX and provenance/quality issues block a credible exact-reference test here; the stale endpoint separately blocks current forward readiness.

The stricter H1 gate failed: exact native SP500 files were absent (micro-labelled files were inspected but not substituted), required USDGBP FX was absent, all files failed the current-within-7-days condition, and individual-contract/vintage/roll provenance was unverified. No portfolio return was calculated, and there is no claimed profitable new candidate. This rejection concerns this tested source/configuration, not every possible free dataset.

A bounded mapping check compared the pinned native SP500 and SP500_micro files on 15,587 valid post-launch overlapping rows: 13,379 prices and 15,417 contract labels matched. Thus 2,208 price rows and 170 contract labels differed; they are not interchangeable tapes. Native metadata also gives USD 50 per point for SP500 versusUSD 5 for SP500_micro. Matching index units is not matching contracts, fills or sizes. This check is now part of the runnable audit; it does not validate the separate provider.

The eight price files are retained privately with hashes and fetch provenance. [Public audit](candidate-data-audit.json) contains metadata only. The gate can run again on its pinned source; adapting another source requires an explicit mapping/version and locked data manifest. Do not fill a missing FX series with1 or treat a changed product label as equivalent by default.

## Concrete next step and completion

Keep H1 as a **data-and-feasibility research protocol**, not a fully validated tradable strategy. Next, establish current read-only access and independently sourced individual-contract/FX vintages for the fixed native universe, then document prospective roll policy, executable timestamps and instrument-specific cost models before any H1 performance run. The MES cost scenario cannot simply be applied to SOFR/CORN/US10. A current Gateway session is not available; no new login/account/paid-data workflow was started.

Pre-2022 is development; 2022–March 2024 is already-opened diagnostic history. Post-March 2024 is a chronological extension, not automatically untouched. The existing 2025–2026 MES cache has already been observed. True prospective evidence begins after registration; no finite shadow period can be accelerated by replaying cached dates. No parameter selection should reuse these data as an untouched holdout.

Three new focused tests passed: independent accounting with synthetic reversals/rolls/gaps, exact mapping/FX/provenance/freshness gate behavior, and missing/duplicate/stale-data detection. The previously passed 37 tests and frozen evaluator are unchanged. The original broker guards, STOP and shadow-only boundary remain; no order sender, exposure increase, scheduler, real trade or account change was introduced.

```bash
python diagnose_strategy.py --upstream /absolute/path/pinned/pysystemtrade --out /private/runtime/diagnostics.json
python audit_candidate_data.py --upstream /absolute/path/pinned/pysystemtrade --out /private/runtime/candidate-data
python -m unittest test_diagnostics -v
```

[Diagnostic evidence](diagnostic-evidence.json) records all outputs, attribution and registration hash. Raw source prices and private broker/account data are excluded.

Sources: [pinned native example](https://github.com/pst-group/pysystemtrade/blob/b4a25e6e1e33a54a3ecfb45c0f6db5e2b60b84f8/systems/provided/example/simplesystemconfig.yaml), [native defaults](https://github.com/pst-group/pysystemtrade/blob/b4a25e6e1e33a54a3ecfb45c0f6db5e2b60b84f8/sysdata/config/defaults.yaml), [Carver on capital/diversification](https://qoppac.blogspot.com/2021/06/static-optimisation-of-best-set-of.html), [AQR original paper](https://www.aqr.com/-/media/AQR/Documents/Insights/Journal-Article/AQR-JPM-Fall-2017.pdf), [audited community dataset](https://github.com/bug-or-feature/pst-csv-data/tree/ef27b05c5d3305834afc4579cef6d8945b6801eb). Checked September 9, 2026.
