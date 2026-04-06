#!/usr/bin/env python3
"""
Simple version archive helper for generated boss skills.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path
from datetime import datetime


TRACKED_FILES = ("persona.md", "work.md", "master-prompt.md", "meta.json")


def archive(skill_dir: Path, version: str) -> Path:
    version_dir = skill_dir / "versions" / version
    version_dir.mkdir(parents=True, exist_ok=True)
    for name in TRACKED_FILES:
        src = skill_dir / name
        if src.exists():
            shutil.copy2(src, version_dir / name)
    return version_dir


def list_versions(skill_dir: Path):
    versions_dir = skill_dir / "versions"
    if not versions_dir.exists():
        return []
    return sorted([p.name for p in versions_dir.iterdir() if p.is_dir()])


def main():
    parser = argparse.ArgumentParser(description="Version manager for generated boss skills")
    parser.add_argument("--action", required=True, choices=["archive", "list"])
    parser.add_argument("--skill-dir", required=True)
    parser.add_argument("--version")
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir)
    if args.action == "archive":
        version = args.version or datetime.now().strftime("v%Y%m%d-%H%M%S")
        print(archive(skill_dir, version))
    else:
        for item in list_versions(skill_dir):
            print(item)


if __name__ == "__main__":
    main()
