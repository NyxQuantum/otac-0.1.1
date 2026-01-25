# OTAC 0.1.2 — Canonical Temporal Attestation Capsule

[

```bash
# Try it from the repo root
curl -sL https://raw.githubusercontent.com/NyxQuantum/otac-0.1.1/main/examples/genesis.json \
  | python -m tools.verify_standalone
```

OTAC = 2 kB JSON that always hashes the same, survives post-quantum attacks, and verifies offline without talking to the original system.

**OTAC 0.1.1** defines a small, canonical evidence object that can be verified **offline** by a court, regulator, PLC or auditor — and that is designed to survive the **post-quantum** era. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)

OTAC is:

- **Canonical** – deterministic JSON (JCS, RFC 8785) and CBOR (RFC 8949) encodings that yield identical canonical hash bytes via a common pipeline. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)
- **Post-quantum ready** – signatures with PQC schemes (e.g. ML-DSA / SLH-DSA), with clear key metadata and entropy provenance hooks. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)
- **Transport-agnostic** – OTAC can be carried over QUIC, TCP, files, messages, PLC channels, etc. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)
- **Offline-verifiable** – a verifier with a single canonical hash + public key can validate an OTAC without talking to the original system. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)
- **Shardable** – optional k-of-n erasure-coded sharding with per-shard headers. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)
- **Open** – essential patent claims are offered under a FRAND-Z (royalty-free) patent license; reference code is under a standard FOSS license. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)

***

## Quick start

### TL;DR — verify an OTAC in seconds

```bash
# 1) Clone and enter the repo
git clone https://github.com/NyxQuantum/otac-0.1.1.git 
cd otac-0.1.1

# 2) (Optional) create a virtualenv and install tooling
python -m venv .venv
# on Windows PowerShell:
#   .venv\Scripts\Activate.ps1
# on Unix-like systems:
#   source .venv/bin/activate

pip install -r requirements.txt

# 3) Verify the sample capsule
python -m tools.verify_standalone examples/genesis.json
```

If the verification succeeds, you will see the canonical HASH / TAC_ID and “OK” for the included post-quantum public key. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)

For a one-liner using a raw file from GitHub (once the repo is public):

```bash
curl -sL https://raw.githubusercontent.com/NyxQuantum/otac-0.1.1/main/examples/genesis.json  \
  | python -m tools.verify_standalone
```

***

## Project layout

Main files and folders:

- `OTAC-0.1.2.md` – human-readable specification (Markdown).
- `OTAC-0.1.1` – previous human-readable specification sources (Markdown / ODT).
- `OTAC-0.1.1.pdf` – rendered specification as a PDF.
- `examples/`
    - `genesis.json` – minimal canonical OTAC example.
    - `test_otac.txt` – sample output from the reference verifier.
- `Vectors/`
    - `vectorA.json` – canonical test vector used in documentation and tests.
- `tools/`
    - `verify_standalone.py` – reference offline verifier (non-production).
    - `README.md` – quick “try in 15 s” instructions focused on the verifier.
- `tests/`
    - regression tests for canonicalisation & verification (pytest).
- `requirements` / `requirements.txt` – Python dependencies for the reference tooling.
- `SECURITY` / `SECURITY.md` – how to report security issues.
- `LICENSE` – open-source license for code and documentation (MIT).
- `PATENT-LICENSE-OTAC` – FRAND-Z patent license for Essential Claims of OTAC 0.1.1.
- `CHANGELOG` – release notes and version history.
- `CONTRIBUTING` – contribution guidelines.
- `Makefile` – helper targets for local tooling and checks. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)

OTAC 0.1.1 is designed to coexist with existing SBOM formats such as CycloneDX: OTAC capsules can reference or embed SBOM identifiers (for example package URLs or component hashes) so that a single attestation object links build artefacts with their CycloneDX metadata. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)

***

## Status and scope

- **Status**: OTAC 0.1.2 is a draft standard and reference implementation (0.1.1 remains available for legacy compatibility). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)
- **Not production code**: `verify_standalone.py` and other tools are intended as reference and for interoperability testing, not as hardened production verifiers. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)
- **Scope**: this repository focuses on the object format and canonicalisation/verification of OTAC capsules. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)

Transport bindings (e.g. QUIC-TAC), PLC integrity (HEC-Sentinel+) and ML provenance pipelines (Dataset Guard) live in other NyxQuantum documents and implementations. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)

***

## Licensing

In practical terms, “FRAND-Z” here means: essential OTAC 0.1.1 patent claims are licensed worldwide on fair, reasonable, **zero-royalty** terms to any conforming implementation. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)

- Essential patent claims … (`PATENT-LICENSE-OTAC`).
- Code and documentation … (`LICENSE` (MIT)).

Using this repository does **not** grant any rights to NyxQuantum trademarks, logos or names. Any such use requires a separate written agreement. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)

***

## Contributing

We welcome contributions that improve interoperability and test coverage: [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)

- new canonical test vectors (please keep each < 64 KiB);
- improved JCS/CBOR compatibility;
- additional verification checks or negative test cases;
- clarifications and errata to `OTAC-0.1.1.md`.

Before opening a pull request, please run:

```bash
pytest
```

By contributing, you agree that your contributions may be incorporated under: [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)

- the open-source license in `LICENSE` for code/text; and
- FRAND-Z terms for any Essential Claims as described in `PATENT-LICENSE-OTAC`.

***

## Security

If you believe you have found a security issue in OTAC 0.1.1 reference code or in the specification, please do **not** open a public issue. Instead, follow the instructions in `SECURITY.md` or contact the maintainer privately. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)

***

## Roadmap & monetisation

- **v0.2** – k-of-n sharding + differential privacy (target: Q2 2026).
- **v0.3** – hardware TQT integration + pre-serialised COSE_Sign1 profiles (target: Q4 2026).
- Commercial layers (EaaS, HEC-Sentinel+, Dataset Guard) remain **NyxQuantum IP** and are licensed separately. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)

***

## Acknowledgements

OTAC 0.1.1 builds on prior work in: [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)

- JSON Canonicalization Scheme (JCS, RFC 8785)
- CBOR (RFC 8949)
- Post-quantum signatures (e.g. ML-DSA, SLH-DSA)
- Secure time synchronisation (NTS, Roughtime, PTP)

and is part of the broader **NyxQuantum** evidence and resilience stack. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63538628/91dae141-bd50-4aa7-8ac4-3561ed3b50bb/README.md)

***

### Cómo pegarlo para que funcione

1. Abre `README.md` en tu editor (VS Code, por ejemplo).  
2. Selecciona todo (Ctrl+A / Cmd+A) y borra.  
3. Pega exactamente el texto anterior desde `# OTAC 0.1.2…` hasta el final.  
4. Guarda y mira la vista previa de Markdown (VS Code: `Ctrl+Shift+V`) o en GitHub tras el push.