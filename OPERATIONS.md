# Bounded paper operations

The shipped profile is disabled. The completed source runtime was flat, had no open orders, and had Gateway read-only restored. No daemon or automatic restart is configured.

## Prepare without orders

Run `python3 configure_local.py` to create a private template and STOP marker outside the repository. The command refuses to overwrite an existing profile. Keep `private_config.yaml` owner-only. Locally populate the exact verified paper account and its single-entry allowlist only after independently checking the simulated environment. Do not put those values in Git.

Use the native environment and PYTHONPATH from REPRODUCE.md. `preflight.py` validates the profile without connecting; `preflight.py --connect-read-only` checks actual identity. Gateway must be the local paper endpoint at 127.0.0.1:4002, with localhost-only access and Read-Only API enabled for preparation.

`fetch_data.py` acquires the selected expiry's daily history. `fetch_continuous.py` acquires signal history through the native client. Data remains local. `native_signal.py` enforces the data gates and computes the native example target. `operate.py` performs read-only order preparation. No stale recorded data ships with the package.

## Intentional finite exercise

A paper exercise requires explicit authorization, a current valid profile, completed data, fresh contract/expiry checks, and a flat account with no existing orders or unrelated positions. Only then may the local STOP marker be intentionally cleared and Gateway paper writes enabled. The command is `operate.py --execute` in the native environment. Do not run it as a scheduler.

The coordinator uses IOC limit orders, at most one contract for entry and one reducing cleanup, a 120-second entry lease and a durable journal. Its marketable limit offset is a test mechanism using delayed quotes, not a execution-quality model. It never uses the historical continuous close as an executable quote.

## Stop and recover

Creating `PAPER_PROJECT_HOME/paper/operation/STOP` blocks new entry while allowing reducing cleanup. Do not kill a process blindly while broker state is uncertain. An ambiguous submission is never retried as a fresh entry. Reconcile broker positions, open orders, executions and the existing journal first; preserve the claim and intent records. An unresolved cleanup or nonflat state requires operator attention, not deletion of the journal or a new run key.

After the finite run, verify flat positions and no open orders with `verify_exit.py`, restore and save Gateway Read-Only API, and recreate STOP. Independent verification and explicit cleanup are required before reporting a clean exit. Shutdown and recovery during an actual pending-network failure remain unproven; this is not a production unattended service.
