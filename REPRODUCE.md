# Reproduce the package

Use Python 3.12 and Git on macOS or Linux. The execution coordinator uses POSIX file locking; Windows needs a compatible environment. Keep the checkout and runtime outside cloud-synced folders. The original native exercise ran on macOS arm64; other platforms need their own verification.

## Safe walkthrough

```sh
python3 demo.py
```

No dependency installation, account or network connection is required.

## Native offline tests

```sh
export PAPER_PROJECT_HOME="$HOME/.local/share/autonomous-trading-research"
python3.12 bootstrap.py pysystemtrade --install
export PYTHONPATH="$PAPER_PROJECT_HOME/upstream/pysystemtrade"
"$PAPER_PROJECT_HOME/venv-pysystemtrade/bin/python" -m unittest test_guards test_operation
```

Bootstrap checks the exact source revision, applies the reviewed connection patch and installs the guard. It preserves an existing mismatched checkout. Dependency files contain version pins, not downloaded package hashes; registry availability and platform compatibility still matter. Bootstrap never starts Gateway or a strategy.

Tests use synthetic data and temporary storage. They do not load a real account profile or connect to a broker. Run them from the repository root.

## Optional Passivbot replay

```sh
python3.12 bootstrap.py passivbot --install
export PYTHONPATH="$PAPER_PROJECT_HOME/upstream/passivbot/src"
cd "$PAPER_PROJECT_HOME/upstream/passivbot"
"$PAPER_PROJECT_HOME/venv-passivbot/bin/python" -c 'from rust_utils import check_and_maybe_compile, verify_loaded_runtime_extension; check_and_maybe_compile(force=True); verify_loaded_runtime_extension()'
"$PAPER_PROJECT_HOME/venv-passivbot/bin/python" -m pytest tests/test_run_fake_live.py
```

Install the upstream-pinned Rust toolchain before building. Follow upstream build prerequisites for the platform. On macOS, wrap behavioral commands in `sandbox-exec -p '(version 1)(allow default)(deny network*)'` after all dependencies are installed. On another platform, use an equivalent network-denied environment and verify that denial; do not call it the same macOS sandbox test.

Use the original config `configs/fake_live_hsl_btc.hjson` and scenarios under `scenarios/fake_live/`, with a fresh fake user and output directory. Example arguments to `src/tools/run_fake_live.py` are `configs/fake_live_hsl_btc.hjson scenarios/fake_live/hsl_long_red_restart.hjson --user reproduction_restart --snapshot-each-step --output-dir /tmp/passivbot-reproduction`. Never reuse a directory holding evidence you intend to preserve.

No broker exercise is part of these reproduction commands. See OPERATIONS.md for the separate, deliberately gated paper workflow.
