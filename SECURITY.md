# Security Policy

## Project status

OTAC 0.1.x is an experimental historical draft and prototype. It is not
production software and does not provide a complete security verifier.

| Surface | Public 0.1.x status |
|---|---|
| JCS serialization and SHA-256 `tac_id` comparison | Prototype implemented |
| Post-quantum signature schema fields | Documented only |
| ML-DSA / SLH-DSA signing or verification | Not implemented |
| Trust, key rotation, and revocation | Not implemented |
| Trusted-time validation | Not implemented |
| Deterministic CBOR and cross-encoding equivalence | Not implemented |
| Sharding and reconstruction | Not implemented |

The appearance of an algorithm name in a schema, example, or historical
specification must not be interpreted as implementation support.

## Supported versions

The `0.1.x` line receives documentation and repository-hygiene corrections only.
There is no supported production release.

## Reporting a vulnerability

Do not open a public issue for a suspected security problem. Send a private
report to **nyxquantum@proton.me**.

Reports are handled on a best-effort basis. This historical prototype has no
guaranteed remediation or disclosure timeline.
