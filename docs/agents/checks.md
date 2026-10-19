# Repository checks

Run from the repository root after `uv sync --locked`:

```powershell
uv run python -m tools.check
```

The command checks acceptance evidence, runs the configured mypy targets, then
runs the complete pytest suite. It stops at the first failed stage. The type
targets include both U6 acceptance scripts and the maintenance tools.

The full suite needs Docker with Linux containers and the isolated query worker.
Build the current source and use its immutable image ID:

```powershell
docker build -t metricguard-check experiments/t02
$env:METRICGUARD_TEST_IMAGE = docker image inspect metricguard-check --format '{{.Id}}'
$env:PYTHONUTF8 = '1'
uv run playwright install chromium
$env:METRICGUARD_BROWSER_CHANNEL = 'chromium'
uv run python -m tools.check
```

The recovery-command test also needs PowerShell (`powershell` on Windows, `pwsh`
on Linux). The Ubuntu GitHub-hosted runner includes PowerShell; CI explicitly
checks it before running tests. On Linux, install Chromium system dependencies with
`uv run playwright install --with-deps chromium`, and export the two environment
variables using the shell's syntax. GitHub Actions builds the worker from the
checkout, installs Chromium, and runs the same command on pushes and pull requests.
It needs no model credentials and makes no live model acceptance calls.

Individual stages are `uv run python -m tools.check evidence`, `types`, or `tests`.
During development, individual test files can still run directly through pytest.
The unified test stage requires the image setting, preserves JUnit under a unique
`artifacts/checks/<run-id>/pytest.xml`, and treats any skipped test as failure.
CI uploads these records even when the checks fail.

## Evidence contract

The evidence stage reads Git-tracked Markdown under `docs/validation/`. For each
local Markdown link or image (including reference-style links), the target must
exist as a file inside the repository and be tracked in the Git index. Stage new
reports and attachments with `git add` before checking; ignored local output is
not a published attachment. Relative links resolve from the report directory;
leading-slash links resolve from the repository root. URL escapes are decoded.

Linked `.gz` files must decompress completely, including checksum/trailer checks.
Compressed `.json.gz` and `.xml.gz` records must also parse in their respective
formats. Historical failed test runs remain valid evidence: this checks the
record's readability, not whether the recorded experiment passed. Failures name
the report, link block's starting line, and target.

External URLs and fragment-only links are not fetched or checked. Links in code
examples are excluded. Raw HTML links and bare paths in prose are outside this
Markdown-link contract. The checker does not verify scientific correctness,
screenshot content, or whether a tracked attachment was pushed remotely.

## Separate live acceptance

`uv run python -m experiments.u6_live` remains an explicitly started, credentialed
live-model acceptance run; it is never invoked by `tools.check` or CI. Human
acceptance remains a separate recorded result. See [local UI](../local-ui.md).
