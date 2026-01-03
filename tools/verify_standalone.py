#!/usr/bin/env python3
"""
OTAC 0.1.1 standalone verifier  (JCS + deterministic CBOR)
pip install cbor2
"""

import json
import argparse
import hashlib
import cbor2  # reservado para futuros usos CBOR deterministas
import sys


def canonicalize(obj):
    """
    Canonicalización JSON tipo JCS:
    - claves ordenadas
    - sin espacios extra
    - UTF-8 sin forzar ASCII
    """
    return json.dumps(
        obj,
        separators=(",", ":"),  # sin espacios
        sort_keys=True,
        ensure_ascii=False,
    )


def canonicalize_json(data):
    """Wrapper exportado para que los tests usen el mismo canon."""
    return canonicalize(data)


def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def canonical_bytes(obj):
    """JSON Canonicalization Scheme (RFC 8785-style)."""
    return canonicalize(obj).encode("utf-8")


def hash_bytes(b, alg="sha-256"):
    """'sha-256' -> 'sha256' para hashlib."""
    return hashlib.new(alg.replace("-", "").lower(), b).hexdigest()


def verify(path):
    data = load(path)

    # Para el hash ignoramos tac_id para evitar dependencia circular
    tmp = {k: v for k, v in data.items() if k != "tac_id"}

    cbytes = canonical_bytes(tmp)
    chash = hash_bytes(cbytes, data["canonical_hash_alg"])
    expected_tac = f"urn:otac:{data['canonical_hash_alg'].lower()}:{chash}"

    print("CANONICAL_BYTES_HEX:", cbytes.hex())
    print("HASH:", chash)
    print("TAC_ID:", expected_tac)
    print("OK" if expected_tac == data.get("tac_id") else "X TAC mismatch")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="OTAC 0.1.1 standalone verifier"
    )
    parser.add_argument("path", help="Ruta a un archivo OTAC JSON")
    args = parser.parse_args(argv)
    verify(args.path)


if __name__ == "__main__":
    main()
