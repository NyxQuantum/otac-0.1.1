import json
from pathlib import Path

from tools.verify_standalone import canonicalize_json, hash_bytes



BASE_DIR = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = BASE_DIR / "examples"


def _load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_canonical_genesis_stable():
    data = _load(EXAMPLES_DIR / "genesis.json")
    c1 = canonicalize_json(data)
    c2 = canonicalize_json(json.loads(c1))
    assert c1 == c2


def test_tac_id_matches_hash_genesis():
    data = _load(EXAMPLES_DIR / "genesis.json")

    # Igual que en verify_standalone.verify: ignoramos tac_id
    tmp = {k: v for k, v in data.items() if k != "tac_id"}

    canonical = canonicalize_json(tmp)

    h = hash_bytes(canonical, data["canonical_hash_alg"])

    assert data["tac_id"] == f"urn:otac:{data['canonical_hash_alg'].lower()}:{h}"


def test_all_examples_parse():
    for name in ["genesis.json", "plc_event.json", "ml_stage.json", "cold_chain.json"]:
        data = _load(EXAMPLES_DIR / name)
        assert "tac_id" in data
        assert "evidence_vector" in data
