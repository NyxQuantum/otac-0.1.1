# OTAC 0.1.x - Known Errata and Limitations

Status: public clarification for the historical 0.1.x line.

This file records defects and ambiguities found after publication. It does not
silently repair the historical specification and does not define OTAC 0.2.

## Normative issues

### E-TBS-01 - Recursive signature input

`OTAC-0.1.2.md` states that the signature covers canonical bytes excluding
`tac_id`, while `pqc_signature.sig` is itself part of the object. Read literally,
the signature value would be included in the bytes used to generate that same
signature. The 0.1.x text therefore does not define a usable, non-recursive
to-be-signed transformation.

**Status:** unresolved in 0.1.x. Do not claim signature conformance.

### E-ID-01 - Identifier semantics are incomplete

The prototype removes only the top-level `tac_id`, canonicalizes the remaining
object, and hashes it. Because the remaining object includes signature-related
fields, 0.1.x does not clearly distinguish an identifier for stable content
from an identifier for a particular signed envelope.

**Status:** unresolved in 0.1.x.

### E-CBOR-01 - Cross-encoding equivalence is not defined

The historical text describes deterministic JSON and deterministic CBOR as
producing identical canonical hash bytes through a common pipeline. The public
repository contains no normative logical data model, complete mapping rules,
CBOR implementation, or cross-encoding vectors that establish this property.

**Status:** unsupported in the public 0.1.x artifacts.

### E-PARSE-01 - Input parsing is not strict

The public verifier uses Python `json.load`. It does not explicitly reject
duplicate member names before conversion to a dictionary and is not a complete
I-JSON/adversarial parser.

**Status:** known limitation.

## Implementation gaps

| ID | Area | Public 0.1.x behavior |
|---|---|---|
| `E-SIG-01` | PQC signatures | No signing or signature verification |
| `E-TRUST-01` | Identity/trust | No key authorization or trust evaluation |
| `E-TIME-01` | Time | `sovereign_time` is data only; no temporal validation |
| `E-LINK-01` | Continuity | `prev_hash_link` is not validated |
| `E-POLICY-01` | Policy | No policy interpretation or compliance decision |
| `E-SHARD-01` | Sharding | No fragmentation, authentication, or recovery |
| `E-CBOR-02` | CBOR | Dependency present, but no CBOR verification path |
| `E-RESULT-01` | Process result | `OK` means only `tac_id` equality; mismatch does not set a non-zero exit code |
| `E-TEST-01` | Tests | Basic regression tests only; no conformance or adversarial suite |

## Interpretation rule

For OTAC 0.1.x, capability labels in a specification, roadmap, schema, example,
or dependency list are design statements unless matching executable code and
tests demonstrate the behavior. A hash match does not establish truth,
provenance, authorization, trusted time, custody, or legal compliance.

