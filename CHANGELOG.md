# Changelog

## Unreleased - Public-scope clarification

- Reclassify OTAC 0.1.x as an experimental historical draft and prototype.
- Document the exact behavior of the public JCS/SHA-256 `tac_id` checker.
- Add normative and implementation errata.
- Remove unsupported public claims of PQC verification, deterministic CBOR,
  sharding, trusted time, and production readiness.
- Correct the quick-start instructions, paths, and CI workflow filename.
- Preserve all historical tags and releases without rewriting them.

## 0.1.3 - 2026-01-25

- Documentation-only release.
- Adds `OTAC-0.1.2.md` and updates the README.
- No code, test, example, or dependency changes from 0.1.2.

## 0.1.2 - 2026-01-24

- Uses the `rfc8785` package for JCS serialization.
- Updates the basic `tac_id` regression tests.
- Does not implement digital-signature verification.

## 0.1.1 - Historical baseline

- Initial public-repository history recorded on 2026-01-05.
- Provides four examples: `genesis`, `plc_event`, `ml_stage`, and
  `cold_chain`.
- Includes schema fields and design text for capabilities not implemented by
  the public verifier.
- No GitHub Release object or immutable `v0.1.1` tag is present in the current
  repository history.
