# OTAC 0.1.x public prototype tools

`verify_standalone.py` is a limited identifier checker. It accepts a JSON file
path, removes the top-level `tac_id`, serializes the remaining object with JCS,
calculates the requested hash, and compares the derived identifier with the
supplied `tac_id`.

```bash
python -m tools.verify_standalone examples/genesis.json
```

`OK` means only that the identifier matches. The tool does not verify a digital
signature, signer trust, time, policy, chain continuity, CBOR, or sharding. See
[`../ERRATA-0.1.x.md`](../ERRATA-0.1.x.md).
