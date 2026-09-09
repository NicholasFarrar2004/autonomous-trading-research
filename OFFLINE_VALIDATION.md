# Passivbot offline validation

The first implementation phase used the existing fake-live scenario runner at pinned Passivbot v8.1.0. It ran against a scripted exchange with network denied on macOS. No credentials, live venue connection or economic backtest were involved.

The baseline/repeat outputs matched. The native terminal scenario originally failed its drawdown assertion: the saved terminal snapshot reported zero rather than the expected full drawdown after terminal fills. The account state was already flat and the stop latch was set, so removing the assertion would have concealed a harness accounting defect.

The isolated patch processes terminal fills before the final snapshot and adds regression coverage. It also corrects the restart fixture's saved metric from zero to 7.5%. The original failing outcome was preserved in local evidence. After correction, the affected harness suite passed 41 tests and the corrected canonical replay matched twice. Strategy, Rust planner and live adapters were not changed.

`passivbot-offline.patch` contains the exact source/test/fixture/changelog changes. `upstreams.json` pins the base; `requirements-passivbot.txt` records resolved Python dependencies. Upstream `rust-toolchain.toml` and Cargo.lock pin Rust inputs; the original run used Rust 1.90.0 on macOS arm64.

To reproduce, prepare the optional upstream using REPRODUCE.md, then run the unchanged scenarios into new output directories. Synthetic account balances and scripted fills test behavior, not returns. Do not transfer cross-venue replay results into a profitability or regional eligibility claim.
