from __future__ import annotations
from pathlib import Path
import argparse

SANDBOX_DB_PATH = Path('/var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3')
CONFIRMATION = 'DELETE_PHASE1B_SANDBOX_DB'

def cleanup_db(db_path: str, confirmation: str, allowed_path: Path = SANDBOX_DB_PATH) -> bool:
    target = Path(db_path)
    if confirmation != CONFIRMATION:
        raise ValueError('explicit_cleanup_confirmation_required')
    if target != allowed_path:
        raise ValueError('sandbox_db_path_mismatch')
    if not target.exists():
        return False
    if not target.is_file():
        raise ValueError('sandbox_db_not_regular_file')
    target.unlink()
    return True

def main() -> int:
    p=argparse.ArgumentParser(description='Delete only the approved Telegram Phase 1B sandbox SQLite DB.')
    p.add_argument('--db', required=True)
    p.add_argument('--confirm', required=True)
    a=p.parse_args()
    deleted=cleanup_db(a.db,a.confirm)
    print('deleted' if deleted else 'already_absent')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
