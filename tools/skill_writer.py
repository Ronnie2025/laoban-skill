#!/usr/bin/env python3
"""
Initialize and update boss skill output folders.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from datetime import datetime, timezone


def init_skill(base_dir: Path, slug: str) -> Path:
    skill_dir = base_dir / slug
    skill_dir.mkdir(parents=True, exist_ok=True)
    for name in ("persona.md", "work.md", "master-prompt.md"):
        path = skill_dir / name
        if not path.exists():
            path.write_text("", encoding="utf-8")

    meta_path = skill_dir / "meta.json"
    if not meta_path.exists():
        meta = {
            "slug": slug,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "version": "v1",
        }
        meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    (skill_dir / "versions").mkdir(exist_ok=True)
    return skill_dir


def main():
    parser = argparse.ArgumentParser(description="Initialize boss skill folder")
    parser.add_argument("--base-dir", default="./bosses")
    parser.add_argument("--slug", required=True)
    args = parser.parse_args()

    skill_dir = init_skill(Path(args.base_dir), args.slug)
    print(skill_dir)


if __name__ == "__main__":
    main()
