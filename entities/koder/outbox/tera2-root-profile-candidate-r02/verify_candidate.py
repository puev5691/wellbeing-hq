from __future__ import annotations
import argparse, hashlib, json, re, subprocess
from pathlib import Path

UPSTREAM_COMMIT = "6cc2061c12986bbaea182786c42d89fd979eeb33"
EXPECTED = {
    "NETWORK": "WELLBEING",
    "SHARD_NAME": "ROOT",
    "NETWORK_ID": "WELLBEING.ROOT",
    "START_NETWORK_DATE": 1800000000000,
    "CONSENSUS_PERIOD_TIME": 3000,
    "START_MINING": 16,
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(base: Path, upstream: Path) -> list[str]:
    profile = json.loads((base / "root-profile.json").read_text())
    local = json.loads((base / "node-local.example.json").read_text())
    patch = (base / "WBN_ROOT_PROFILE.patch").read_text()
    checks = []

    assert profile["upstream_commit"] == UPSTREAM_COMMIT
    assert profile["chain_identity"]["NETWORK"] == EXPECTED["NETWORK"]
    assert profile["chain_identity"]["SHARD_NAME"] == EXPECTED["SHARD_NAME"]
    assert profile["chain_identity"]["NETWORK_ID"] == EXPECTED["NETWORK_ID"]
    assert profile["temporal_identity"]["START_NETWORK_DATE"] == EXPECTED["START_NETWORK_DATE"]
    assert profile["temporal_identity"]["CONSENSUS_PERIOD_TIME"] == EXPECTED["CONSENSUS_PERIOD_TIME"]
    assert profile["reward_mining_policy"]["START_MINING"] == EXPECTED["START_MINING"]
    assert profile["candidate_boundaries"]["runtime_launch"] is False
    assert profile["candidate_boundaries"]["existing_DATA_DB_mutation"] is False
    assert profile["candidate_boundaries"]["credentials"] is False
    checks.append("profile_contract")

    forbidden_chain_fields = {"NETWORK", "SHARD_NAME", "NETWORK_ID", "START_NETWORK_DATE", "CONSENSUS_PERIOD_TIME"}
    assert forbidden_chain_fields.isdisjoint(local)
    assert local["USE_MINING"] is False
    assert local["required_preflight"]["DATA_shard_js_absent"] is True
    checks.append("chain_vs_node_local_separation")

    assert 'case "WBN_ROOT"' in patch
    assert 'global.NETWORK = "WELLBEING"' in patch
    assert 'global.SHARD_NAME = "ROOT"' in patch
    assert 'global.START_NETWORK_DATE = 1800000000000' in patch
    assert 'global.START_MINING = 16' in patch
    assert 'Name:"WBN system reserve"' in patch
    assert 'SumCOIN:TOTAL_SUPPLY_TERA' in patch
    assert "DATA/shard.js" not in patch
    assert "global.USE_MINING = 1" not in patch
    checks.append("patch_contract")

    scan_names = [
        "root-profile.json", "node-local.example.json", "WBN_ROOT_PROFILE.patch",
        "UPSTREAM-EVIDENCE.md", "CANDIDATE-CHOICES.md", "README.md", "SOURCE-IDENTITIES.json",
    ]
    combined = "\n".join((base / name).read_text(errors="ignore") for name in scan_names)
    assert "-----BEGIN PRIVATE KEY-----" not in combined
    assert "-----BEGIN RSA PRIVATE KEY-----" not in combined
    assert not re.search(r"(?i)(private[_ -]?key|secret)\s*[:=]\s*[A-Za-z0-9+/=_-]{24,}", combined)
    checks.append("no_secret_material")

    head = subprocess.check_output(["git", "-C", str(upstream), "rev-parse", "HEAD"], text=True).strip()
    assert head == UPSTREAM_COMMIT
    subprocess.run(["git", "-C", str(upstream), "apply", "--check", str(base / "WBN_ROOT_PROFILE.patch")], check=True)
    checks.append("patch_applies_to_exact_upstream")

    sums = base / "SHA256SUMS.txt"
    if sums.exists():
        for line in sums.read_text().splitlines():
            digest, name = line.split("  ", 1)
            assert sha256(base / name) == digest, name
        checks.append("checksums")
    return checks


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--upstream", required=True)
    args = ap.parse_args()
    checks = verify(Path(__file__).resolve().parent, Path(args.upstream).resolve())
    print("PASS", len(checks), ",".join(checks))


if __name__ == "__main__":
    main()
