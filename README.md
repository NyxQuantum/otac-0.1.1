# OTAC 0.1.2 — Canonical Temporal Attestation Capsule

![CI](https://github.com/NyxQuantum/otac-0.1.1/actions/workflows/ci.yml/badge.svg)

```bash
# Try it from the repo root (≈15 s)
curl -sL https://raw.githubusercontent.com/NyxQuantum/otac-0.1.1/main/examples/genesis.json \
  | python -m tools.verify_standalone
```

OTAC is a ~2 kB JSON evidence capsule that always hashes the same and verifies offline without talking to the original system.

OTAC 0.1.2 defines a small, canonical evidence object that can be verified offline by a court, regulator, PLC or auditor — and that is designed to survive the post-quantum era.

OTAC is:
- **Canonical** – deterministic JSON (JCS, RFC 8785) and CBOR (RFC 8949) encodings that yield identical canonical hash bytes via a common pipeline. 
- **Post-quantum ready** – signatures with PQC schemes (e.g. ML-DSA / SLH-DSA), with clear key metadata and entropy provenance hooks
- **Transport-agnostic** – OTAC can be carried over QUIC, TCP, files, messages, PLC channels, etc.
- **Offline-verifiable** – a verifier with a single canonical hash + public key can validate an OTAC without talking to the original system.
- **Shardable** – optional k-of-n erasure-coded sharding with per-shard headers. 
- **Open** – essential patent claims are offered under a FRAND-Z (royalty-free) patent license; reference code is under a standard FOSS license.***

## Quick start

### TL;DR — verify an OTAC in seconds

```bash
# 1) Clone and enter the repo
git clone https://github.com/NyxQuantum/otac-0.1.1.git
cd otac-0.1.1

# 2) (Optional) create a virtualenv and install tooling
python -m venv .venv
# on Windows PowerShell: .venv\Scripts\Activate.ps1
# on Unix-like systems: source .venv/bin/activate

pip install -r requirements.txt

# 3) Verify the sample capsule
python -m tools.verify_standalone examples/genesis.json
```

If the verification succeeds, you will see the canonical HASH / TAC_ID and “OK” for the included post-quantum public key.
***

## Project layout

Main files and folders:

- `OTAC-0.1.2.md` – human-readable specification (Markdown).
- `OTAC-0.1.1.md` – legacy spec (kept for backwards reference).
- `OTAC-0.1.1.pdf` – rendered legacy PDF (B/W friendly).
- `vectors/` – test vectors and reference examples.
- `examples/`
- `genesis.json` – minimal canonical OTAC example.  
- `test_otac.txt` – sample output from the reference verifier. 
- `tools/`
- `verify_standalone.py` – reference offline verifier (non-production).
- `tests/` – regression tests for canonicalisation & verification (pytest).
- `requirements.txt` – Python dependencies for the reference tooling.
- `SECURITY.md` – how to report security issues. 
- `LICENSE` – open-source license for code and documentation (MIT). 
- `PATENT-LICENSE-OTAC` – FRAND-Z patent license for Essential Claims of OTAC 0.1.x. 
- `CHANGELOG` – release notes and version history.
- `CONTRIBUTING.md` – contribution guidelines.
- `Makefile` – helper targets for local tooling and checks.

OTAC 0.1.2 is designed to coexist with existing SBOM formats such as CycloneDX: OTAC capsules can reference or embed SBOM identifiers (for example package URLs or component hashes) so that a single attestation object links build artefacts with their CycloneDX metadata. 
***

## Status and scope

- **Status**: OTAC 0.1.2 is a draft standard and reference implementation (0.1.1 remains available for legacy compatibility). 
- **Not production code**: `verify_standalone.py` and other tools are intended as reference and for interoperability testing, not as hardened production verifiers.
- **Scope**: this repository focuses on the object format and canonicalisation/verification of OTAC capsules. Transport bindings (e.g. QUIC-TAC), PLC integrity (HEC-Sentinel+), and ML provenance pipelines (Dataset Guard) live in other NyxQuantum documents and implementations.
***

## Licensing

Patent license: FRAND-Z for Essential Claims covering the OTAC 0.1.x specification family (see `PATENT-LICENSE-OTAC`). 
- Code and documentation: `LICENSE` (MIT).
Using this repository does **not** grant any rights to NyxQuantum trademarks, logos or names. Any such use requires a separate written agreement
***

## Contributing

We welcome contributions that improve interoperability and test coverage:

- new canonical test vectors (please keep each < 64 KiB),
- improved JCS/CBOR compatibility,
- additional verification checks or negative test cases,
- clarifications and errata to `OTAC-0.1.2.md` as PRs. 
Before opening a pull request, please run:

```bash
pytest
```

By contributing, you agree that your contributions may be incorporated under:

- the open-source license in `LICENSE` for code/text, and
- FRAND-Z terms for any Essential Claims as described in `PATENT-LICENSE-OTAC`.
***

## Security

If you discover a security issue in OTAC 0.1.2, please do **not** open a public issue. Instead, follow the instructions in `SECURITY.md` or contact the maintainer privately
***

## Roadmap & monetisation

- **v0.2** – k-of-n sharding + differential privacy (target: Q2 2026).
- **v0.3** – hardware TQT integration + pre-serialised COSE_Sign1 profiles (target: Q4 2026).
- Commercial layers (EaaS, HEC-Sentinel+, Dataset Guard) remain **NyxQuantum IP** and are licensed separately
***

## Acknowledgements

OTAC builds on prior work in:

- JSON Canonicalization Scheme (JCS, RFC 8785)
- CBOR (RFC 8949)
- Post-quantum signatures (e.g. ML-DSA, SLH-DSA)
- Secure time synchronisation (NTS, Roughtime, PTP)

```