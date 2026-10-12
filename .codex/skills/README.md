# Project skill snapshot

This directory tracks the 27 skills already installed for MetricGuard, including
their `SKILL.md`, supporting templates, scripts, references and `agents/openai.yaml`
metadata. Keeping these files together preserves relative references and the
project's engineering workflow when another contributor clones the repository.

Source: https://github.com/mattpocock/skills

Upstream commit: `49dd158d1076134a641b33efb035946536778336`

At baseline creation, all 79 installed files matched their corresponding files in
the upstream checkout's `skills/engineering/` or `skills/productivity/` directories
byte for byte. The upstream MIT license is included as `LICENSE`.

Tracked skills:

- ask-matt
- code-review
- codebase-design
- diagnosing-bugs
- domain-modeling
- grill-me
- grill-with-docs
- grilling
- handoff
- implement
- implement-spec
- improve-codebase-architecture
- pr
- prototype
- research
- retro
- setup-matt-pocock-skills
- tdd
- teach
- to-questionnaire
- to-spec
- to-tickets
- triage
- wait-what
- wayfinder
- wizard
- writing-for-agents

The root `skills/` directory is a local upstream Git checkout, not project source;
it is ignored and is not a submodule. Machine-specific `.codex/` configuration and
runtime state are also ignored. Future skill additions or local modifications
should be reviewed explicitly; upstream updates are not applied automatically.

Project-specific configuration lives in `AGENTS.md` and `docs/agents/`.
