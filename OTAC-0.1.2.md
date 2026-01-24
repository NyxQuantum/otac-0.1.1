# OTAC 0.1.2 — Canonical Temporal Attestation Capsule (JCS/CBOR, PQC) with Test Vectors and FRAND‑Z Terms

VERSION: 0.1.2  
DATE: January 2026  
AUTHORS: Project NyxQuantum (Sigitas Andrijauskas Sumlinskas, et al.)  
CONTACT: NyxQuantum@proton.me  

STATUS OF THIS DOCUMENT:  
- Public specification with patent pending  
- Normative only where stated  
- FRAND‑Z licensing offer for Essential Claims

---

## Abstract

OTAC (Canonical Temporal Attestation Capsule) defines a canonical, signed temporal evidence object with offline verifiability, dual deterministic encodings (JSON/CBOR), a common canonicalization pipeline producing identical canonical bytes, optional erasure‑coded sharding, and hooks for Temporal Quorum Time (TQT) and Evidence‑as‑a‑Service (EaaS).[file:12]

OTAC is transport‑agnostic and may be encapsulated in files, messages, or streams without changing its canonical definition.[file:12]

---

## Table of Contents

1. Scope and Goals  
2. Terminology and Normative Language  
3. OTAC Data Model  
   3.1 Required Fields  
   3.2 Optional Fields  
   3.3 Encoding Constraints and Limits  
4. Canonicalization (Normative)  
   4.1 Canonical Object Structure  
   4.2 Canonical Hash and TAC_ID Derivation  
   4.3 Post‑Quantum Signature  
   4.4 Temporal Evidence (Optional)  
   4.5 Sharding (Optional)  
5. Canonical Profiles (v0.1.2)  
6. Interoperability (TQT, EaaS, QUICTAC, PoPCam, COSE/JOSE)  
7. Security and Privacy Considerations  
8. Offline Verification Procedure (Normative)  
9. Test Vectors Templates  
10. FRAND‑Z Licensing Terms  
11. References  
Appendix A. Minimal verify.py Template  
Appendix B. Vector Files Layout  

---

## 1. Scope and Goals

This document specifies OTAC 0.1.2, a canonical temporal evidence object for critical systems.[file:12]

Goals include: deterministic canonicalization (JSON/CBOR), post‑quantum‑ready signatures, offline verification, and support for custody chains and sharding.[file:12]

Non‑goals include defining transport semantics (congestion control, multiplexing, quorum logic, or policy engines).[file:12]

---

## 2. Terminology and Normative Language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **NOT RECOMMENDED**, **MAY**, and **OPTIONAL** in this document are to be interpreted as described in RFC 2119 and RFC 8174 when, and only when, they appear in all capitals.[file:12]

JSON uses UTF‑8; CBOR uses deterministic encoding per RFC 8949; time values use UTC “Z” and RFC 3339.[file:12]

**Canonical Bytes**: Deterministic byte representation of an OTAC object following RFC 8785 (JSON) or deterministic CBOR (RFC 8949 Section 4.2).[file:12]

---

## 3. OTAC Data Model

An OTAC is a structured object with required and optional fields.[file:12]

### 3.1 Required Fields

- `version` (string): OTAC specification version (here `"0.1.2"`).  
- `canonical_profile_id` (string, URN): locks canonical ordering and normalization rules.  
- `canonical_hash_alg` (string): hash algorithm used for canonical hash (MUST be `"SHA-256"` in 0.1.2).  
- `policy_id` (string): policy profile identifier.  
- `sovereign_time` (string, UTC RFC 3339): attested issuance time.  
- `identity_anchor` (object or string): certificate/anchor digest, DID reference, or equivalent trust anchor.  
- `prev_hash_link` (hex string): hash of prior OTAC canonical bytes using `canonical_hash_alg`; genesis MUST be all‑zero hex of digest length.[file:12]  
- `evidence_vector` (object/array): domain‑specific evidence payload (minimised).  
- `policy_digest` (hex string): digest over the policy snapshot used for this OTAC.  
- `pqc_signature` (object): post‑quantum signature (see Section 4.3).  
- `tac_id` (string, URN): stable identifier derived from canonical hash (see Section 4.2).[file:12]

### 3.2 Optional Fields

Optional fields include (non‑exhaustive):[file:12]

- `shard_header`: index/total/params for k‑of‑n shards.  
- `shard_auth_tag`: per‑shard MAC/signature to authenticate shards before reassembly.  
- `privacy_stamp`: privacy budget stamp (e.g., epsilon, delta, k, scope).  
- `lineage_id`: identifier linking related OTACs across a process or pipeline.  
- `tqt_meta`: time‑quorum provenance (sources, weights, path‑asymmetry bounds).  
- `quantum_entropy_provenance`: randomness source and health record.  
- `compliance_stamp`: compliance profile IDs (e.g., DORA/IEC 62443 mappings).  
- `content_type`: short type for `evidence_vector` (e.g., `pop`, `hec`, `ml-stage`).  
- `key_rotation_info`: hints about key rotation policy and related keys.[file:12]

### 3.3 Encoding Constraints and Limits

- Deterministic JSON per RFC 8785; deterministic CBOR per RFC 8949.  
- All strings MUST be NFC Unicode; timestamps MUST be UTC “Z” RFC 3339.  
- Numbers MUST be finite; NaN/Inf are forbidden.  
- Recommended non‑normative maximum OTAC size is 64 KiB; larger payloads SHOULD use external references with hash pointers in `evidence_vector`.[file:12]  
- `canonical_profile_id` SHOULD correspond to a published, integrity‑protected profile definition; verifiers SHOULD maintain an allow‑list and MUST NOT silently downgrade to weaker profiles.[file:12]

---

## 4. Canonicalization (Normative)

OTAC defines canonical bytes for hashing, identifier generation, and signature input.[file:12]

### 4.1 Canonical Object Structure

Both JSON and CBOR encodings feed a common normalization pipeline identified by `canonical_profile_id`, yielding identical canonical bytes for the same logical object.[file:12]

Let `canonical_bytes` be the output of this pipeline.

### 4.2 Canonical Hash and TAC_ID Derivation

#### 4.2.1 Canonicalization Pipeline

For OTAC 0.1.2, canonical representation MUST follow:

#### JSON canonical form (JCS)

When `canonical_profile_id` indicates JSON, implementations MUST canonicalize JSON using the **JSON Canonicalization Scheme (JCS), RFC 8785**.

- Implementations MUST produce UTF‑8 canonical bytes per RFC 8785.  
- Implementations MUST NOT use ad‑hoc `json.dumps(... sort_keys=...)` as a substitute for RFC 8785 compliance.

#### CBOR canonical form (Deterministic)

When `canonical_profile_id` indicates CBOR, implementations MUST encode CBOR in a deterministic form (Deterministic CBOR as per RFC 8949 guidance for canonical/deterministic encoding).

#### 4.2.2 TAC_ID derivation (Normative)

`tac_id` MUST be derived from the canonical hash of the OTAC object **excluding** the `tac_id` field itself.

1. Let `O` be the OTAC JSON object.  
2. Let `O'` be `O` with the `tac_id` member removed (if present).  
3. Compute `canonical_bytes = canonicalize(O')` using the canonicalization rules of this version.  
4. Compute `hash = SHA-256(canonical_bytes)` (hex lowercase).  
5. Set:

`tac_id = "urn:otac:sha-256:" + <hex(hash)>`

This replaces the informal “ignore tac_id” wording in 0.1.1 and normalizes TAC identifier derivation.[file:12]

#### 4.2.3 Normative Requirements

- `canonical_hash_alg` MUST be `"SHA-256"` in version 0.1.2.  
- Future versions MAY support additional algorithms (e.g., SHA‑512/256, SHA3‑256, BLAKE3).  
- The same OTAC MUST produce identical `canonical_hash` regardless of source encoding (JSON/CBOR), programming language, operating system, or whitespace/formatting in original input.[file:12]

### 4.3 Post‑Quantum Signature

The `pqc_signature` object provides post‑quantum cryptographic authentication.[file:12]

**Structure (JSON):**

```json
{
  "alg": "ML-DSA",
  "param_set": "ML-DSA-65",
  "sig": "a3f2c1...",
  "key_id": "urn:otac:key:issuer:2026-01"
}
```

- `alg` (string, REQUIRED): `"ML-DSA"` or `"SLH-DSA"`.  
- `param_set` (string, REQUIRED): e.g., `"ML-DSA-44"`, `"ML-DSA-65"`, `"ML-DSA-87"`, `"SLH-DSA-128s"`.  
- `sig` (string, REQUIRED): signature bytes (JSON: lowercase hex; CBOR: byte string).  
- `key_id` (string, OPTIONAL): URN/URI identifying public key.[file:12]

Conformant OTAC 0.1.2 implementations:

- **MUST** support: `ML-DSA-65` (NIST FIPS 204, dilithium3).  
- **SHOULD** support: `ML-DSA-44` for resource‑constrained environments.  
- **MAY** support: `ML-DSA-87`, `SLH-DSA-128s`, `SLH-DSA-128f`.[file:12]

The signature MUST cover the canonical bytes computed as per Section 4.2, ensuring integrity of all fields except `tac_id` (which is derived from the hash).[file:12]

### 4.4 Temporal Evidence (Optional)

The `time_evidence` object provides cryptographic proof of the temporal anchor.

#### Structure

```json
{
  "sovereign_time": "2026-01-22T17:00:00.000Z",
  "time_evidence": {
    "type": "TQT",
    "assurance_level": "high",
    "proof": "base64url...",
    "sources": 3
  }
}
```

#### Fields

- `type` (string, REQUIRED):  
  - `"claim"` — timestamp claim (no cryptographic proof)  
  - `"NTS"` — Network Time Security (RFC 8915)  
  - `"Roughtime"` — Roughtime protocol  
  - `"TQT"` — Temporal Quorum Time (multi‑source consensus)

- `assurance_level` (string, REQUIRED):  
  - `"none"` — no cryptographic proof (claim‑only)  
  - `"basic"` — single authenticated source with verifiable proof  
  - `"high"` — multi‑source quorum/consensus with verifiable proof

- `proof` (string, REQUIRED if `assurance_level != "none"`):  
  Base64url‑encoded proof blob (format depends on `type`), MUST be verifiable by an independent party.

- `sources` (integer, OPTIONAL):  
  Number of time sources used; REQUIRED for `type: "TQT"`.

#### Semantics

- If `time_evidence` is absent: `sovereign_time` is claim‑only (equivalent to `assurance_level = "none"`).  
- If present: verifiers MUST validate `proof` according to `type`.  
- Verifiers MAY reject OTACs with insufficient assurance for their use case.

#### Interoperability

- Implementations MUST NOT invent custom assurance levels in v0.1.2.  
- Only `"none"`, `"basic"`, `"high"` are permitted.  
- Future versions may define additional levels if needed.

### 4.5 Sharding (Optional)

OTACs MAY be split into k‑of‑n erasure‑coded shards for resilience.[file:12]

**`shard_header` structure:**

```json
{
  "shard_index": 0,
  "total_shards": 5,
  "threshold": 3,
  "shard_algorithm": "reed-solomon",
  "parent_tac_id": "urn:otac:sha256:abc123..."
}
```

Details of sharding algorithms and reconstruction are profile‑dependent.[file:12]

---

## 5. Canonical Profiles (v0.1.2)

A `canonical_profile_id` defines normative requirements for OTAC conformance.[file:12]

This version introduces normative `canonical_profile_id` values:

- `urn:otac:profile:core:v1`  
- `urn:otac:profile:plc-integrity:v1`  
- `urn:otac:profile:ml-provenance:v1`

A profile defines REQUIRED vs OPTIONAL fields, accepted encodings, and conformance requirements.

### 5.1 Profile: Core v1

**Identifier**: `urn:otac:profile:core:v1`  

**Purpose**: Baseline OTAC for general‑purpose temporal attestation.

**Required Fields (for this profile)** include at least:

- `version`: `"0.1.2"`  
- `canonical_profile_id`: `"urn:otac:profile:core:v1"`  
- `canonical_hash_alg`: `"SHA-256"`  
- `sovereign_time`  
- `identity_anchor`  
- `prev_hash_link`  
- `evidence_vector`  
- `policy_digest`  
- `pqc_signature`  
- `tac_id`.[file:12]

(Other profiles – `plc-integrity` and `ml-provenance` – refine these requirements for their verticals and may add further constraints on `evidence_vector`, `content_type`, and sharding usage.)[file:12]

---

## 6. Interoperability (TQT, EaaS, QUICTAC, PoPCam, COSE/JOSE)

- **TQT**: When available, `tqt_meta` SHOULD list sources (NTS/PTP/NTP/other), trust weights, and path‑asymmetry bounds; `time_evidence` binds this into a verifiable structure.[file:12]  
- **EaaS**: Custody services MAY ingest OTACs, verify timestamps versus TQT, reseal them with PQC signatures, and retain erasure‑coded copies under tenant isolation.[file:12]  
- **QUICTAC / PoPCam**: Systems MAY reference `tac_id` or embed summaries of `evidence_vector`, keeping full OTAC records off‑path where appropriate.[file:12]  
- **COSE/JOSE**: Implementations MAY wrap `pqc_signature` in COSE_Sign1 or JWS; signatures MUST always be over canonical bytes.[file:12]

---

## 7. Security and Privacy Considerations

Topics include replay protection via `prev_hash_link`, canonicalization pitfalls and profile allow‑lists, key rotation at service layer, data minimization in `evidence_vector`, privacy budgets via `privacy_stamp`, and entropy provenance for PQC signatures.[file:12]

Implementations MUST use cryptographically secure RNGs suitable for PQC key and signature generation.[file:12]

---

## 8. Offline Verification Procedure (Normative)

Given an OTAC object:

1. Validate field presence and lengths (`version`, `canonical_profile_id`, `canonical_hash_alg`, etc.).  
2. Canonicalize to bytes via the pipeline referenced by `canonical_profile_id` (Section 4).  
3. Recompute `tac_id` as per Section 4.2 and compare to provided `tac_id`.  
4. Recompute `prev_hash_link` from the previous OTAC’s canonical bytes and compare (if not genesis).  
5. Build domain‑separated input and verify `pqc_signature.sig` using provisioned public key material.  
6. If sharded, authenticate shards, reassemble, then repeat steps above on the reconstructed OTAC.  
7. Optionally validate `time_evidence` and `tqt_meta` against local temporal policy.[file:12]

---

## 9. Test Vectors Templates

The reference package includes JSON/CBOR examples (genesis, PLC event, ML stage, cold chain) with canonical bytes and expected hashes/tac_ids.[file:12]

---

## 10. FRAND‑Z Licensing Terms (Summary)

- Royalty‑free, worldwide, non‑exclusive license to Essential Claims needed to implement OTAC 0.1.2 conformant with this document.  
- Reciprocity: each implementer grants an equivalent royalty‑free license to its Essential Claims covering OTAC 0.1.2.  
- Defensive suspension against entities initiating offensive patent actions.  
- No trademark rights; provided “AS IS”.[file:12]

(Full text in `PATENT-LICENSE-OTAC.txt` in the reference package.)

---

## 11. Legacy Canonical Profile IDs

The following canonical profile ID remains valid for OTAC 0.1.1 compatibility:

- `urn:otac:canon:2025-11-26:jcs-cbor-v1` (legacy)

New implementations SHOULD prefer `urn:otac:profile:*` identifiers in v0.1.2.

---

## 12. References

Normative and informative references match OTAC 0.1.1 (RFC 8785, RFC 8949, RFC 3339, RFC 2119/8174, NIST PQC, erasure codes, ISO/IEC 19790, COSE/JOSE, RATS, etc.).[file:12]

---

Appendix A and B follow the same structure as in OTAC 0.1.1, updated where necessary to reference version 0.1.2 and the new canonical profiles.[file:12]
```
