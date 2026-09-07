# OTAC 0.2 — Technical Assessment and Project Closure

**Status:** Research note — not a specification, standard, conformance profile, security product, or legal/compliance statement  
**Assessment date:** 7 September 2026  
**Public code reviewed:** [NyxQuantum/otac-0.1.1](https://github.com/NyxQuantum/otac-0.1.1), default branch as retrieved on the assessment date

## Executive decision

OTAC is closed as an active protocol and product-development line.

The public `0.1.x` repository should remain an honest historical prototype. No
OTAC `0.2` protocol release is planned. In this document, “OTAC 0.2” names the
assessment that closes the project; it does not designate a new implementation
or normative format.

This is not a finding that the original problem was imaginary. Portable,
independently verifiable evidence is a real engineering problem. The closure
decision follows from a narrower conclusion:

1. the public implementation proves only deterministic JSON serialization and
   a SHA-256-derived identifier for the supplied examples;
2. the historical specification contains unresolved normative defects;
3. mature standards already cover most of the proposed primitives;
4. newer SCITT work overlaps directly with the strongest remaining generic
   concept—portable composite evidence and structured verification results;
5. turning OTAC into a useful interoperability toolkit would require substantial
   implementation, conformance, security, and maintenance work; and
6. no reviewed evidence establishes a user, deployment, or differentiator strong
   enough to justify that opportunity cost.

The rational outcome is therefore **NO-GO for further OTAC development** and
**GO for preserving its useful technical lessons**.

| Question | Assessment |
|---|---|
| Is the underlying evidence problem real? | Yes |
| Is OTAC 0.1.x a complete evidence verifier? | No |
| Should OTAC become a new universal evidence format? | No |
| Could an interoperability toolkit be engineered? | Yes, technically |
| Is that the best use of current effort? | No evidence that it is |
| What should survive? | The public historical record, limitations, and reusable design lessons |

## 1. Premises and assessment method

This assessment applies the following rules:

- A documented field or goal is **proposed**, not implemented, unless executable
  code and tests demonstrate it.
- A matching hash proves byte-level integrity under the implemented transform;
  it does not prove authorship, authority, trusted time, provenance, truth,
  completeness, custody, or policy compliance.
- Standards are compared by capability, not by name or marketing language.
- The absence of reviewed adoption or user evidence is stated as an evidence
  gap, not as proof that no interest can exist.
- The decision includes opportunity cost: technically possible work is not
  automatically work worth doing.
- External standards and drafts are assessed as of 7 September 2026. An
  Internet-Draft is not treated as an RFC or as IETF consensus.

The assessment is based on the public repository, its errata, the historical
`0.1.2` text, its checker and regression tests, and the primary sources listed
at the end of this note. It does not evaluate private implementations or make
legal or regulatory conclusions.

## 2. What OTAC intended to solve

The historical design attempted to define a portable evidence capsule combining
several concerns:

- deterministic representation and content addressing;
- digital signatures, including post-quantum signatures;
- signer identity and trust anchors;
- temporal evidence;
- links between successive records;
- policy references and domain-specific evidence;
- offline verification;
- JSON/CBOR portability; and
- optional sharding and recovery.

Each concern is legitimate. The problem is their combination into a new generic
envelope without complete semantics, an interoperable implementation, or a
validated adoption path. The breadth increased both the claim surface and the
number of security decisions that had to be correct at once.

## 3. What the public 0.1.x prototype actually implements

The repository [now describes its limits clearly](https://github.com/NyxQuantum/otac-0.1.1/blob/main/README.md).
Its [executable checker](https://github.com/NyxQuantum/otac-0.1.1/blob/main/tools/verify_standalone.py):

1. parses a JSON file;
2. removes the top-level `tac_id` member;
3. serializes the remaining object using JCS ([RFC 8785](https://www.rfc-editor.org/rfc/rfc8785));
4. hashes those bytes with SHA-256;
5. constructs `urn:otac:sha-256:<digest>`; and
6. compares that value with the supplied `tac_id`.

The [current regression suite](https://github.com/NyxQuantum/otac-0.1.1/blob/main/tests/test_otac.py)
contains three basic tests: JCS stability for one example, one expected
`tac_id`, and parsing/presence checks for four examples.

| Capability | Public 0.1.x status | Consequence |
|---|---|---|
| JCS serialization | Implemented for JSON examples | Useful narrow prototype |
| SHA-256 `tac_id` comparison | Implemented | Detects mismatch under that transform |
| Digital-signature verification | Not implemented | No signer authenticity |
| ML-DSA or SLH-DSA | Schema/documentation only | No public PQC verification claim |
| Identity and key authorization | Not implemented | An identifier is not a trust decision |
| Trusted or historical time | Not implemented | Time fields are unverified data |
| Previous-record continuity | Not implemented | No verified chain property |
| Policy evaluation | Not implemented | No compliance or acceptance result |
| Deterministic CBOR path | Not implemented | Cross-encoding claim is unproven |
| Sharding and recovery | Not implemented | No resilience property |
| Strict adversarial parsing | Not implemented | Duplicate-key and parser ambiguity remain |
| Conformance/adversarial suite | Not implemented | Interoperability and security are untested |

One operational defect is especially concrete: the checker prints a mismatch
but does not return a non-zero process status. It is therefore unsafe to treat
the command as a pass/fail security gate.

## 4. Material design defects in the historical specification

These are not cosmetic gaps; they prevent a reliable independent
implementation of the proposed security behavior. They are also recorded in
the repository's [public errata](https://github.com/NyxQuantum/otac-0.1.1/blob/main/ERRATA-0.1.x.md).

### 4.1 Recursive to-be-signed input

The [historical `0.1.2` text](https://github.com/NyxQuantum/otac-0.1.1/blob/main/OTAC-0.1.2.md)
says that the signature covers the canonical object excluding
`tac_id`, while the signature value remains inside that object. Read literally,
the signature would be part of the bytes from which the same signature must be
created. No usable, non-recursive to-be-signed transformation is defined.

### 4.2 Ambiguous identifier semantics

Because the object remaining after removal of `tac_id` contains
signature-related fields, the identifier does not clearly distinguish stable
content from a particular signed envelope. Those are different identities and
often require different identifiers.

### 4.3 Unsupported JSON/CBOR equivalence

JCS JSON and deterministic CBOR are different encodings and do not naturally
produce identical bytes. A common logical data model, complete mapping rules,
one normative signing representation, and cross-implementation vectors would
be required. The public artifacts provide none of these.

### 4.4 Metadata is not verification

Fields for identity, time, policy, continuity, or algorithm choice do not
establish those properties. A verifier must define trust roots, protected
headers, authorization, freshness, revocation, failure behavior, and the exact
evidence required for each conclusion.

### 4.5 Results are too coarse

`OK` currently means only that one derived identifier matches. It does not
separate syntax, content binding, signature validity, issuer authorization,
time, revocation, completeness, or policy. Collapsing those axes encourages a
false assurance conclusion.

## 5. Existing standards occupy most of the design space

OTAC would not enter an empty field. The relevant comparison is the composition
of existing standards and ecosystems.

| Need | Existing work | Implication for OTAC |
|---|---|---|
| Standard signed envelopes and protected headers | JOSE and COSE, including [COSE structures in RFC 9052](https://www.rfc-editor.org/rfc/rfc9052) | A new signature envelope needs exceptional justification |
| Post-quantum signatures in standard envelopes | [RFC 9964](https://www.rfc-editor.org/rfc/rfc9964) registers ML-DSA-44/65/87 for JOSE and COSE | PQC representation is no longer a generic differentiator |
| Signed statements, transparency, and portable receipts | [SCITT, RFC 9943](https://www.rfc-editor.org/rfc/rfc9943) | Do not build an incompatible statement/receipt system |
| Portable composite evidence, profiles, offline verification, conflicts, and rich result codes | [SCITT Composite Evidence Verification draft](https://datatracker.ietf.org/doc/draft-nobuo-scitt-composite-evidence-verification/) | Direct overlap with the strongest proposed OTAC 0.2 pivot |
| Software provenance and attestations | [in-toto Statement](https://in-toto.io/Statement/v1) and [Sigstore verification](https://docs.sigstore.dev/cosign/verifying/verify/) | Reuse subjects, predicates, signatures, logs, timestamps, and bundles |
| Media provenance and detailed validation outcomes | [C2PA 2.2](https://spec.c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html) | Another established domain model already separates validation states and codes |
| Trusted timestamp tokens | [RFC 3161](https://www.rfc-editor.org/rfc/rfc3161) | A timestamp string should not replace signed temporal evidence |
| Long-term evidence preservation | [Evidence Record Syntax, RFC 4998](https://www.rfc-editor.org/rfc/rfc4998) | Hash trees and renewal mechanisms pre-exist OTAC |
| Attestation evidence, appraisal, and results | [RATS architecture, RFC 9334](https://www.rfc-editor.org/rfc/rfc9334) | Evidence and acceptance results should remain distinct |

Two qualifications matter:

1. SCITT does not prove that a statement is true. RFC 9943 explicitly frames
   transparency as accountability and auditability, with receipts that can be
   verified without contacting the transparency service.
2. The composite-verification document is an individual Internet-Draft dated
   July 2026. It has no formal IETF standing and may change or expire. Even so,
   it already specifies the generic territory most likely to justify OTAC 0.2:
   portable bundles, online/offline verification, issuer and freshness rules,
   missing or conflicting evidence, graph digests, and structured results.

This does not make all future engineering pointless. It makes a new generic
OTAC format strategically weak. The defensible contribution would have to be a
tested implementation, adapter, profile, or domain result—not the broad
architecture alone.

## 6. Alternatives evaluated

| Route | Technical feasibility | Differentiation | Required effort | Decision |
|---|---:|---:|---:|---|
| Extend 0.1.x into a complete verifier | Medium | Low | High | **NO-GO** |
| Publish OTAC 0.2 as a universal proprietary capsule | Medium | Low | High | **NO-GO** |
| Pivot OTAC into a standards-interoperability toolkit | Medium–high | Low conceptually; potentially useful in execution | Medium–high and ongoing | **NO-GO now** |
| Preserve 0.1.x and publish this assessment | High | Honest historical/research value | Low | **SELECTED** |

The interoperability-toolkit route was previously a reasonable conditional
experiment. It is not selected now because its value would depend on substantial
new code, negative test corpora, multi-implementation interoperability,
maintenance against evolving standards, and validation by an external user.
None of those assets currently exists in the reviewed public line. Pursuing the
route would also delay projects that may have a clearer vertical problem.

## 7. Residual technical value

Closing the project does not require discarding everything learned. The
following ideas remain useful as engineering lessons, without being claimed as
unique inventions:

- Content addressing and authenticity are separate properties.
- A valid signature and a trusted signer are separate results.
- Trusted time requires evidence and policy, not a self-declared timestamp.
- Evidence presence, evidence validity, completeness, and domain truth are
  separate questions.
- Offline verification requires the necessary trust material, policies,
  receipts, and revocation or freshness information to travel with—or be
  explicitly unavailable to—the verifier.
- `UNKNOWN`, `MISSING`, `STALE`, `CONFLICT`, and `UNSUPPORTED` are necessary
  outcomes; a verifier must not manufacture `PASS` from incomplete knowledge.
- New formats should be justified only after an existing standard cannot
  express a concrete, tested requirement.
- A specification should be driven by byte-exact vectors, negative cases, and
  independent implementations before broad capability claims.

The most valuable OTAC output is therefore not another envelope. It is a clear
record of why assurance systems must separate observation, statement,
cryptographic validation, trust, policy, and decision.

## 8. Closure boundaries

The closure decision has the following practical meaning:

1. **No OTAC 0.2 specification or implementation will be released.** This
   assessment is the only artifact carrying the `0.2` label.
2. **OTAC 0.1.x remains frozen as historical.** Maintenance is limited to
   security notices, factual clarification, dead-link repair, and repository
   hygiene—not feature development.
3. **No universal-format claims.** OTAC should not be described as a standard,
   production verifier, forensic-grade system, complete PQC implementation, or
   proof of truth/compliance.
4. **No dependency inheritance.** D-TAC, AEGIS, NXQ-04, or any later project
   must not depend on OTAC simply to preserve continuity. They should use
   relevant standards directly and justify every new layer independently.
5. **No hidden roadmap.** Proposed features such as a new TBS, dual JSON/CBOR
   semantics, custom signatures, sharding, temporal quorum, policy engines, or
   universal result vectors are not deferred OTAC commitments.
6. **No rewriting history.** Existing tags and historical documents remain
   available with their notices and errata.

The GitHub repository may remain technically unarchived until the D-TAC review
checks whether any small, non-protocol code or fixtures are worth reusing. That
temporary state must not be interpreted as active OTAC development. If D-TAC
does not require direct reuse, archiving the repository is appropriate.

## 9. Rules for future reuse

Future projects may reuse lessons, generic test techniques, or ordinary utility
code after review. They should not inherit OTAC's unresolved semantics.

| May be reused after review | Must not be inherited by default |
|---|---|
| Clear implemented/proposed distinction | `tac_id` semantics |
| JCS test technique or generic fixtures | Historical TBS transformation |
| Negative assurance taxonomy | OTAC JSON/CBOR equivalence claim |
| Documentation and errata discipline | Custom trust/time/compliance claims |
| Fail-closed test cases | OTAC as a mandatory dependency or umbrella brand |

For D-TAC in particular, the initial question should be independent of OTAC:
does a concrete ML workflow need a signed, portable audit export that existing
tools do not already provide in a usable form? Only evidence from that audit
should decide whether D-TAC proceeds.

## 10. Risks after closure

| Risk | Control |
|---|---|
| Readers mistake this note for a new specification | Keep the status banner and avoid normative protocol language |
| Historical feature lists are read as implementation claims | Link prominently to the README and errata |
| Later projects quietly recreate OTAC | Require a standalone problem statement and standards comparison for each project |
| The report becomes stale as standards evolve | Preserve the assessment date; update only factual references, not the historical decision |
| Closure is misread as “the problem has no value” | State clearly that the NO-GO concerns this architecture and opportunity cost |

## 11. Open questions

No open technical question blocks closure. Two repository-management decisions
remain, and neither reopens the project:

1. After the D-TAC code inventory, is there any generic utility or fixture worth
   copying without carrying OTAC semantics?
2. Once that check is complete, should the GitHub repository be marked archived?

## 12. Recommended GitHub publication steps

After one human review:

1. add this file at the repository root as
   `OTAC-0.2-TECHNICAL-ASSESSMENT.md`;
2. add one short README link under the existing status notice;
3. add a documentation-only CHANGELOG entry recording project closure;
4. do not alter historical tags or describe this note as release `0.2`; and
5. decide repository archival only after the D-TAC reuse check.

## References

- OTAC public historical repository: [NyxQuantum/otac-0.1.1](https://github.com/NyxQuantum/otac-0.1.1)
- RFC 8785: [JSON Canonicalization Scheme](https://www.rfc-editor.org/rfc/rfc8785)
- RFC 9052: [CBOR Object Signing and Encryption (COSE): Structures and Process](https://www.rfc-editor.org/rfc/rfc9052)
- RFC 9943: [An Architecture for Trustworthy and Transparent Digital Supply Chains](https://www.rfc-editor.org/rfc/rfc9943)
- RFC 9964: [ML-DSA for JOSE and COSE](https://www.rfc-editor.org/rfc/rfc9964)
- IETF individual draft: [Composite Evidence Verification for SCITT Statement Graphs](https://datatracker.ietf.org/doc/draft-nobuo-scitt-composite-evidence-verification/)
- Sigstore: [Verifying signatures and bundles](https://docs.sigstore.dev/cosign/verifying/verify/)
- in-toto: [Statement v1](https://in-toto.io/Statement/v1)
- C2PA: [Technical Specification 2.2](https://spec.c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html)
- RFC 3161: [Time-Stamp Protocol](https://www.rfc-editor.org/rfc/rfc3161)
- RFC 4998: [Evidence Record Syntax](https://www.rfc-editor.org/rfc/rfc4998)
- RFC 9334: [Remote ATtestation procedureS Architecture](https://www.rfc-editor.org/rfc/rfc9334)

---

**Final project state:** OTAC active development closed; public `0.1.x`
preserved as a historical experimental prototype; no `0.2` protocol release.
