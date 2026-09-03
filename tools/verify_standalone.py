#!/usr/bin/env python3
"""Limited OTAC 0.1.x JCS/SHA-256 ``tac_id`` checker.

This historical prototype does not verify signatures, trust, time, CBOR,
continuity, policy, or sharding. See ``ERRATA-0.1.x.md``.
"""

import json
import rfc8785
import argparse
import hashlib
import cbor2  # reservado para futuros usos CBOR deterministas
import sys


def canonicalize(obj):
    """
    JSON Canonicalization Scheme (RFC 8785).
    Devuelve bytes UTF-8 canónicos.
    """
    return rfc8785.dumps(obj)





def canonicalize_json(data):
    """Convenience: canonical bytes de un dict JSON."""
    return canonicalize(data)  # canonicalize ya devuelve bytes



def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def canonical_bytes(obj):
    """JSON Canonicalization Scheme (RFC 8785)."""
    return canonicalize(obj)



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
