# OTAC 0.1.1 – Post-Quantum Evidence Capsule

> 2 kB JSON/CBOR blob that a court, PLC or regulator can verify offline – and that survives the quantum era.

```bash
# test from GitHub (no clone) – test in ~15 s
curl -sL https://raw.githubusercontent.com/NyxQuantum/otac/main/examples/genesis.json | python3 tools/verify_standalone.py

# test locally after cloning – also ~15 s
python3 tools/verify_standalone.py examples/genesis.json