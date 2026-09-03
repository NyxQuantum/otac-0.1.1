# OTAC 0.1.x - Historical Experimental Draft

![CI](https://github.com/NyxQuantum/otac-0.1.1/actions/workflows/ci.yml/badge.svg)

> **Status notice:** OTAC 0.1.x is preserved as an experimental historical
> draft and prototype. It is not a production implementation, a conformance
> claim, or the current design baseline for future OTAC work. Read
> [`ERRATA-0.1.x.md`](ERRATA-0.1.x.md) before using the specification or code.

This repository demonstrates a small part of the OTAC concept: deterministic
JSON serialization with JCS (RFC 8785), SHA-256 hashing, and comparison of a
derived `tac_id` for the included examples.

## What the public prototype does

- parses the supplied JSON example;
- removes the top-level `tac_id` field;
- serializes the remaining object with JCS using `rfc8785`;
- calculates a SHA-256 digest;
- derives `urn:otac:sha-256:<digest>`;
- compares that value with the supplied `tac_id`.

## What the public prototype does not do

The repository does **not** currently implement or validate:

- ML-DSA, SLH-DSA, or any other digital signature;
- signer identity, key authorization, trust, rotation, or revocation;
- historical or trusted time;
- `prev_hash_link` continuity;
- policy semantics or legal/regulatory compliance;
- deterministic CBOR or JSON/CBOR equivalence;
- erasure-coded sharding or shard reconstruction;
- strict duplicate-key rejection or a complete adversarial parser;
- truth, provenance, or correctness of the evidence being hashed.

Some of these mechanisms appear in the historical specification as design
goals or schema fields. Their presence in a document or example is not evidence
that the public verifier implements them.

## Quick start

```bash
git clone https://github.com/NyxQuantum/otac-0.1.1.git
cd otac-0.1.1

python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# Unix-like shell: source .venv/bin/activate

python -m pip install -r requirements.txt
python -m tools.verify_standalone examples/genesis.json
```

The command prints `HASH`, the derived `TAC_ID`, and either `OK` or
`X TAC mismatch`. In this prototype, `OK` means only that the supplied
`tac_id` matches the locally recalculated JCS/SHA-256 identifier. It does not
mean that a signature, identity, timestamp, chain, or policy has been verified.

Run the limited regression tests with:

```bash
python -m pytest tests/ -q
```

## Version history

| Version | Role | Code status |
|---|---|---|
| `0.1.1` | Historical initial draft | Superseded by the 0.1.2 prototype |
| `0.1.2` | JCS/SHA-256 `tac_id` prototype | Public technical baseline for 0.1.x |
| `0.1.3` | Documentation-only release | No code, test, example, or dependency changes from 0.1.2 |

The tags and releases remain available for traceability. No historical tag is
rewritten by this clarification.

## Repository layout

- `OTAC-0.1.2.md` - historical 0.1.2 specification draft.
- `OTAC-0.1.1.md` and `OTAC-0.1.1.pdf` - legacy 0.1.1 draft.
- `ERRATA-0.1.x.md` - known normative and implementation limitations.
- `tools/verify_standalone.py` - limited JCS/SHA-256 identifier checker.
- `scripts/otac-cli.py` - non-functional signing/verifying CLI placeholder.
- `examples/` - illustrative JSON capsules.
- `Vectors/` - historical vector material; not a conformance suite.
- `tests/` - limited regression tests.
- `LICENSE.txt` - MIT license for the repository material.
- `PATENT-LICENSE-OTAC.txt` - separate patent-license text whose exact terms
  should be read directly; no broader rights should be inferred from this
  README.

## Scope and future work

OTAC 0.1.x is frozen as a historical line. Future OTAC work is being designed
separately and must not be inferred from this repository. No roadmap date or
future capability is promised here.

## Security

Do not use this prototype to make production security, compliance, custody, or
forensic-assurance decisions. See [`SECURITY.md`](SECURITY.md) for reporting
instructions and the supported scope.

## References

- [RFC 8785 - JSON Canonicalization Scheme](https://www.rfc-editor.org/rfc/rfc8785)
- [FIPS 180-4 - Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)
