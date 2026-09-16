from __future__ import annotations
import argparse, hashlib, json, re, shutil, subprocess, tempfile
from decimal import Decimal
from pathlib import Path
from typing import Any

UPSTREAM_COMMIT = "6cc2061c12986bbaea182786c42d89fd979eeb33"
UPSTREAM_REPOSITORY = "https://gitlab.com/terafoundation/tera2.git"
COMMON_SECTIONS = (
    "chain_identity", "temporal_identity", "consensus_schedule", "protocol_updates",
    "genesis_public_config", "reward_mining_policy", "candidate_boundaries",
)

class VerificationError(RuntimeError):
    pass

def require(ok: bool, code: str) -> None:
    if not ok:
        raise VerificationError(code)

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load_json(path: Path) -> Any:
    return json.loads(path.read_text())

def jget(obj: Any, path: str) -> Any:
    cur = obj
    for part in path.split("."):
        cur = cur[part]
    return cur

def leaf_paths(value: Any, prefix: str) -> set[str]:
    if isinstance(value, dict):
        out: set[str] = set()
        for key, child in value.items():
            out |= leaf_paths(child, f"{prefix}.{key}" if prefix else key)
        return out
    return {prefix}

def resolve_file(base: Path, value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else base / path

def git_output(args: list[str], cwd: Path | None = None) -> str:
    return subprocess.check_output(args, cwd=cwd, text=True).strip()

def parse_js_literal(expr: str) -> Any:
    expr = expr.strip()
    if expr.startswith(('"', "'")):
        if expr.startswith("'"):
            return expr[1:-1]
        return json.loads(expr)
    if re.fullmatch(r"-?\d+", expr):
        return int(expr)
    if re.fullmatch(r"-?\d+(?:\.\d+)?[eE][+-]?\d+", expr):
        val = Decimal(expr)
        return int(val) if val == int(val) else val
    raise VerificationError(f"unsupported_js_literal:{expr}")

def extract_case_block(text: str, case_value: str) -> str:
    marker = f'case "{case_value}":'
    start = text.find(marker)
    require(start >= 0, f"selector_case_missing:{case_value}")
    tail = text[start + len(marker):]
    m = re.search(r"\n\s*break\s*;", tail)
    require(m is not None, f"selector_case_break_missing:{case_value}")
    return tail[:m.start()]

def global_assignments(case_block: str) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for symbol, expr in re.findall(r"global\.([A-Za-z0-9_]+)\s*=\s*([^;]+);", case_block):
        out[symbol] = parse_js_literal(expr)
    return out

def touched_patch_files(patch: str) -> set[str]:
    pairs = re.findall(r"^diff --git a/(\S+) b/(\S+)$", patch, flags=re.M)
    require(all(a == b for a, b in pairs), "patch_path_pair_mismatch")
    return {a for a, _ in pairs}

def source_blob(upstream: Path, path: str) -> str:
    row = git_output(["git", "-C", str(upstream), "ls-tree", "HEAD", "--", path])
    parts = row.split()
    require(len(parts) >= 3, f"source_missing:{path}")
    return parts[2]

def verify_source_identities(upstream: Path, source_ids: dict[str, Any]) -> None:
    require(git_output(["git", "-C", str(upstream), "rev-parse", "HEAD"]) == UPSTREAM_COMMIT, "upstream_head_mismatch")
    require(source_ids.get("upstream_commit") == UPSTREAM_COMMIT, "source_manifest_upstream_commit_mismatch")
    for path, ident in source_ids.items():
        if path == "upstream_commit":
            continue
        require(source_blob(upstream, path) == ident["git_blob"], f"source_blob_mismatch:{path}")
        require(sha256(upstream / path) == ident["sha256"], f"source_sha256_mismatch:{path}")

def materialize_post_patch(base: Path, upstream: Path, patch_path: Path, expected_files: set[str]) -> Path:
    temp = Path(tempfile.mkdtemp(prefix="tera2-r03-postpatch-"))
    try:
        for rel in expected_files:
            dst = temp / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(upstream / rel, dst)
        subprocess.run(["git", "apply", "--check", str(patch_path)], cwd=temp, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        subprocess.run(["git", "apply", str(patch_path)], cwd=temp, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return temp
    except Exception:
        shutil.rmtree(temp, ignore_errors=True)
        raise

def verify_post_patch_identities(post: Path, patched_ids: dict[str, Any], touched: set[str]) -> None:
    require(set(patched_ids) == touched, "postpatch_identity_file_set_mismatch")
    for path, ident in patched_ids.items():
        require(git_output(["git", "hash-object", str(post / path)]) == ident["git_blob_after_patch"], f"postpatch_blob_mismatch:{path}")
        require(sha256(post / path) == ident["sha256_after_patch"], f"postpatch_sha256_mismatch:{path}")

def map_coverage(policy_map: dict[str, Any]) -> set[str]:
    covered = {policy_map["selector"]["profile_path"]}
    covered |= {x["profile_path"] for x in policy_map["source_assignments"]}
    covered |= {x["profile_path"] for x in policy_map["derived"]}
    covered |= {x["profile_path"] for x in policy_map["upstream_constants"]}
    g = policy_map["genesis_semantics"]
    covered |= {g[k] for k in (
        "system_balance_profile_path", "zero_range_profile_path", "founder_profile_path",
        "developer_profile_path", "supply_profile_path",
    )}
    covered |= {x["profile_path"] for x in policy_map["patch_invariants"]}
    covered |= {x["profile_path"] for x in policy_map["policy_only"]}
    return covered

def verify_policy_coverage(profile: dict[str, Any], policy_map: dict[str, Any]) -> None:
    expected = {"mode_run"}
    for section in COMMON_SECTIONS:
        expected |= leaf_paths(profile[section], section)
    covered = map_coverage(policy_map)
    require(covered == expected, "policy_map_leaf_coverage_mismatch")

def verify_node_local(profile: dict[str, Any], local: dict[str, Any]) -> None:
    forbidden = {"MODE_RUN", "NETWORK", "SHARD_NAME", "NETWORK_ID", "START_NETWORK_DATE", "CONSENSUS_PERIOD_TIME"}
    require(forbidden.isdisjoint(local), "node_local_common_selector_forbidden")
    require(local.get("common_profile_selector_ref") == "root-profile.json#mode_run", "node_local_selector_ref_mismatch")
    require(local.get("USE_MINING") is False, "node_local_mining_must_default_false")
    pre = local.get("required_preflight", {})
    require(pre.get("DATA_shard_js_absent") is True, "node_local_shard_absence_preflight_missing")
    require(pre.get("mode_run_from_common_profile") is True, "node_local_mode_derivation_preflight_missing")
    require(profile["mode_run"] == "WBN_ROOT", "profile_mode_run_mismatch")

def verify_assignments(profile: dict[str, Any], policy_map: dict[str, Any], patched_const: str) -> None:
    selector = policy_map["selector"]
    require(selector["expected"] == profile[selector["profile_path"]], "selector_profile_mismatch")
    block = extract_case_block(patched_const, selector["expected"])
    assignments = global_assignments(block)
    for item in policy_map["source_assignments"]:
        expected = jget(profile, item["profile_path"])
        actual = assignments.get(item["source_symbol"], object())
        require(actual == expected, f"assignment_mismatch:{item['profile_path']}")
    return block

def verify_derived(profile: dict[str, Any], policy_map: dict[str, Any]) -> None:
    for item in policy_map["derived"]:
        if item["proof"] == "concat":
            value = item.get("separator", "").join(str(jget(profile, p)) for p in item["inputs"])
            require(jget(profile, item["profile_path"]) == value, f"derived_mismatch:{item['profile_path']}")
        else:
            raise VerificationError(f"unsupported_derived_proof:{item['proof']}")

def parse_upstream_numeric(text: str, symbol: str) -> Any:
    m = re.search(rf"global\.{re.escape(symbol)}\s*=\s*([^;]+);", text)
    require(m is not None, f"upstream_symbol_missing:{symbol}")
    return parse_js_literal(m.group(1))

def verify_upstream_constants(profile: dict[str, Any], policy_map: dict[str, Any], upstream: Path) -> None:
    for item in policy_map["upstream_constants"]:
        text = (upstream / item["source_file"]).read_text()
        actual = parse_upstream_numeric(text, item["source_symbol"])
        require(actual == jget(profile, item["profile_path"]), f"upstream_constant_mismatch:{item['profile_path']}")

def extract_wbn_genesis_branch(accounts_text: str) -> str:
    marker = 'if(global.MODE_RUN === "WBN_ROOT")'
    start = accounts_text.find(marker)
    require(start >= 0, "wbn_genesis_branch_missing")
    brace = accounts_text.find("{", start)
    require(brace >= 0, "wbn_genesis_branch_open_brace_missing")
    depth = 0
    for i in range(brace, len(accounts_text)):
        if accounts_text[i] == "{": depth += 1
        elif accounts_text[i] == "}":
            depth -= 1
            if depth == 0:
                return accounts_text[brace + 1:i]
    raise VerificationError("wbn_genesis_branch_unbalanced")

def verify_genesis(profile: dict[str, Any], policy_map: dict[str, Any], post: Path, upstream: Path) -> None:
    g = policy_map["genesis_semantics"]
    accounts = (post / g["source_file"]).read_text()
    branch = extract_wbn_genesis_branch(accounts)
    constant = (upstream / g["genesis_count_source_file"]).read_text()
    m = re.search(r"global\.BLOCK_PROCESSING_LENGTH\s*=\s*(\d+)\s*;", constant)
    require(m is not None, "block_processing_length_missing")
    length = int(m.group(1))
    require(re.search(r"global\.BLOCK_PROCESSING_LENGTH2\s*=\s*BLOCK_PROCESSING_LENGTH\s*\*\s*2\s*;", constant) is not None, "block_processing_length2_formula_mismatch")
    count = length * 2
    require(count == g["expected_genesis_count"] == 16, "genesis_count_mismatch")
    supply = jget(profile, g["supply_profile_path"])
    require(jget(profile, g["system_balance_profile_path"]) == supply, "genesis_system_allocation_mismatch")
    require(jget(profile, g["zero_range_profile_path"]) == 0, "genesis_zero_range_profile_mismatch")
    require(jget(profile, g["founder_profile_path"]) == 0, "genesis_founder_preallocation_mismatch")
    require(jget(profile, g["developer_profile_path"]) == 0, "genesis_developer_preallocation_mismatch")
    require(re.search(r"Num:0[^\n]*SumCOIN:TOTAL_SUPPLY_TERA", branch) is not None, "genesis_system_source_mismatch")
    require(re.search(r"for\s*\(var i = 1; i < BLOCK_PROCESSING_LENGTH2; i\+\+\)", branch) is not None, "genesis_zero_range_loop_missing")
    require(re.search(r"Num:i[^\n]*Value:\{BlockNum:1\}[^\n]*Name:\"\"", branch) is not None, "genesis_zero_range_write_mismatch")
    require(re.search(r"\breturn\b", branch) is not None, "genesis_branch_return_missing")
    require(accounts.find('if(global.MODE_RUN === "WBN_ROOT")') < accounts.find('Name:"Founder account"'), "genesis_branch_order_mismatch")

def verify_invariants(profile: dict[str, Any], local: dict[str, Any], policy_map: dict[str, Any], patch: str, wbn_block: str, touched: set[str], source_ids: dict[str, Any]) -> None:
    for item in policy_map["patch_invariants"]:
        path, proof = item["profile_path"], item["proof"]
        require(jget(profile, path) == item["expected"], f"invariant_profile_mismatch:{path}")
        if proof == "patch_forbids_text":
            require(item["text"] not in patch, f"patch_forbidden_text:{path}")
        elif proof == "patch_no_global_assignment_and_node_local_false":
            require(re.search(rf"global\.{re.escape(item['source_symbol'])}\s*=", wbn_block) is None, f"runtime_mining_source_assignment_forbidden:{path}")
            require(local.get("USE_MINING") is False, f"runtime_mining_node_local_not_false:{path}")
        elif proof == "package_secret_scan":
            pass
        elif proof == "source_unchanged_and_patch_untouched":
            require(item["source_file"] not in touched, f"retained_source_touched:{item['source_file']}")
            require(item["source_file"] in source_ids, f"retained_source_identity_missing:{item['source_file']}")
        else:
            raise VerificationError(f"unsupported_invariant_proof:{proof}")

def verify_policy_only(profile: dict[str, Any], policy_map: dict[str, Any]) -> None:
    for item in policy_map["policy_only"]:
        require(jget(profile, item["profile_path"]) == item["expected"], f"policy_only_mismatch:{item['profile_path']}")

def verify_secret_scan(base: Path) -> None:
    names = [
        "root-profile.json", "node-local.example.json", "POLICY-MAP.json", "WBN_ROOT_PROFILE.patch",
        "SOURCE-IDENTITIES.json", "PATCHED-FILE-IDENTITIES.json", "UPSTREAM-EVIDENCE.md",
        "CANDIDATE-CHOICES.md", "README.md",
        "fixtures/negative-node-mode-mismatch.json", "fixtures/negative-profile-consensus-mismatch.json",
    ]
    combined = "\n".join((base / name).read_text(errors="ignore") for name in names)
    require("-----BEGIN PRIVATE KEY-----" not in combined, "private_key_material_detected")
    require("-----BEGIN RSA PRIVATE KEY-----" not in combined, "rsa_private_key_material_detected")
    require(not re.search(r"(?i)(private[_ -]?key|secret)\s*[:=]\s*[A-Za-z0-9+/=_-]{24,}", combined), "secret_like_material_detected")

def verify_checksums(base: Path) -> None:
    sums = base / "SHA256SUMS.txt"
    if not sums.exists():
        return
    for line in sums.read_text().splitlines():
        digest, name = line.split("  ", 1)
        require(sha256(base / name) == digest, f"checksum_mismatch:{name}")

def verify(base: Path, upstream: Path, *, profile_file: str | Path = "root-profile.json", node_local_file: str | Path = "node-local.example.json") -> list[str]:
    profile = load_json(resolve_file(base, profile_file))
    local = load_json(resolve_file(base, node_local_file))
    policy_map = load_json(base / "POLICY-MAP.json")
    source_ids = load_json(base / policy_map["identity_files"]["source"])
    patched_ids = load_json(base / policy_map["identity_files"]["post_patch"])
    patch_path = base / "WBN_ROOT_PROFILE.patch"
    patch = patch_path.read_text()
    checks: list[str] = []

    require(profile.get("upstream_repository") == UPSTREAM_REPOSITORY, "upstream_repository_mismatch")
    require(profile.get("upstream_commit") == UPSTREAM_COMMIT, "profile_upstream_commit_mismatch")
    require(profile.get("profile") == "WBN_ROOT_R03", "profile_version_mismatch")
    checks.append("profile_metadata")

    verify_policy_coverage(profile, policy_map); checks.append("policy_map_full_leaf_coverage")
    verify_node_local(profile, local); checks.append("mode_selector_fail_closed")
    verify_source_identities(upstream, source_ids); checks.append("pinned_source_identities")

    touched = touched_patch_files(patch)
    require(touched == set(policy_map["required_patch_files"]), "patch_file_set_mismatch")
    post = materialize_post_patch(base, upstream, patch_path, touched)
    try:
        verify_post_patch_identities(post, patched_ids, touched); checks.append("declared_postpatch_identities")
        patched_const = (post / "Source/core/const-mode.js").read_text()
        wbn_block = verify_assignments(profile, policy_map, patched_const); checks.append("full_policy_source_assignments")
        verify_derived(profile, policy_map); checks.append("derived_chain_identity")
        verify_upstream_constants(profile, policy_map, upstream); checks.append("upstream_constants")
        verify_genesis(profile, policy_map, post, upstream); checks.append("full_genesis_accounts_0_15")
        verify_invariants(profile, local, policy_map, patch, wbn_block, touched, source_ids); checks.append("patch_invariants")
        verify_policy_only(profile, policy_map); checks.append("policy_only_boundaries")
    finally:
        shutil.rmtree(post, ignore_errors=True)

    verify_secret_scan(base); checks.append("no_secret_material")
    verify_checksums(base)
    if (base / "SHA256SUMS.txt").exists(): checks.append("checksums")
    return checks

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--upstream", required=True)
    ap.add_argument("--profile", default="root-profile.json")
    ap.add_argument("--node-local", default="node-local.example.json")
    args = ap.parse_args()
    try:
        checks = verify(Path(__file__).resolve().parent, Path(args.upstream).resolve(), profile_file=args.profile, node_local_file=args.node_local)
    except VerificationError as exc:
        print("FAIL", str(exc))
        raise SystemExit(1)
    print("PASS", len(checks), ",".join(checks))

if __name__ == "__main__":
    main()
