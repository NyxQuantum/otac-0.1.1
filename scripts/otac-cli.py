#!/usr/bin/env python3
"""
otac-cli – stub CLI for OTAC 0.1.1

Planned future usage (not implemented yet):

  ./scripts/otac-cli.py sign   input.json  priv.key
  ./scripts/otac-cli.py verify input.json  pub.key

For now, this is only a placeholder that prints what it *would* do.
No real PQC signing or verification is performed yet.
"""

import argparse
import sys
from pathlib import Path


def cmd_sign(args: argparse.Namespace) -> None:
    print("Future use (not implemented yet): sign OTAC JSON with real PQC keys.")
    print(f"[stub] Would sign file: {args.file} with key: {args.key}")
    sys.exit(0)


def cmd_verify(args: argparse.Namespace) -> None:
    print("Future use (not implemented yet): verify OTAC JSON with real PQC keys.")
    print(f"[stub] Would verify file: {args.file} with key: {args.key}")
    sys.exit(0)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="otac-cli stub for OTAC 0.1.1 (no real PQC yet)."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # sign
    p_sign = subparsers.add_parser("sign", help="(stub) sign an OTAC JSON file")
    p_sign.add_argument("file", type=Path, help="Input OTAC JSON file")
    p_sign.add_argument("key", type=Path, help="Private key file (future use)")
    p_sign.set_defaults(func=cmd_sign)

    # verify
    p_verify = subparsers.add_parser("verify", help="(stub) verify an OTAC JSON file")
    p_verify.add_argument("file", type=Path, help="Input OTAC JSON file")
    p_verify.add_argument("key", type=Path, help="Public key file (future use)")
    p_verify.set_defaults(func=cmd_verify)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
