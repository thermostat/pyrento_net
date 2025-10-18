#!/usr/bin/env python3
"""
Sync the Quarto `_site` build output into the GitHub Pages repository.

By default the script looks for the user-site repo at ../thermostat.github.io
relative to this repository. Pass an explicit path to override the target.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], cwd: Path, check: bool = True) -> subprocess.CompletedProcess:
    """Run a command and return the CompletedProcess."""
    return subprocess.run(cmd, cwd=cwd, check=check, text=True, capture_output=True)


def ensure_clean_repo(repo: Path) -> None:
    """Abort if the repo has uncommitted changes."""
    status = run(["git", "status", "--porcelain"], cwd=repo)
    if status.stdout.strip():
        sys.stderr.write(f"Refusing to continue: {repo} has uncommitted changes.\n")
        sys.stderr.write(status.stdout)
        sys.exit(1)


def copy_tree(src: Path, dst: Path) -> None:
    """Copy contents of src into dst (dst may already exist)."""
    for item in src.iterdir():
        target = dst / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            shutil.copy2(item, target)


def main() -> int:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[1]

    quarto_site_root = repo_root / "quarto_site" / "pyrento"
    site_dir = quarto_site_root / "_site"
    if not site_dir.is_dir():
        sys.stderr.write(f"Expected build output at {site_dir}; run `quarto render` first.\n")
        return 1

    default_target = repo_root.parent / "thermostat.github.io"

    parser = argparse.ArgumentParser(
        description="Copy Quarto _site output into the thermostat.github.io repository."
    )
    parser.add_argument(
        "target",
        nargs="?",
        type=Path,
        default=default_target,
        help=f"Path to the user-site repository (default: {default_target})",
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Push the updated site to origin after committing.",
    )
    args = parser.parse_args()

    target_repo = args.target.resolve()
    if not target_repo.is_dir():
        sys.stderr.write(f"Target repository {target_repo} does not exist.\n")
        return 1
    if not (target_repo / ".git").exists():
        sys.stderr.write(f"{target_repo} does not appear to be a git repository.\n")
        return 1

    ensure_clean_repo(target_repo)

    # Record the hash of this repository's HEAD for the commit message.
    head_proc = run(["git", "rev-parse", "HEAD"], cwd=repo_root)
    source_sha = head_proc.stdout.strip()

    # Remove everything in the target repo except the .git directory.
    for entry in target_repo.iterdir():
        if entry.name == ".git":
            continue
        if entry.is_dir():
            shutil.rmtree(entry)
        else:
            entry.unlink()

    copy_tree(site_dir, target_repo)

    run(["git", "add", "."], cwd=target_repo)

    diff = run(["git", "status", "--short"], cwd=target_repo)
    if not diff.stdout.strip():
        print("No changes detected in target repository; nothing to commit.")
        return 0

    commit_message = f"Site update from pyrento_net {source_sha[:7]}"
    run(["git", "commit", "-m", commit_message], cwd=target_repo)
    print(f"Committed site update in {target_repo} with message:\n  {commit_message}")

    if args.push:
        run(["git", "push"], cwd=target_repo)
        print("Pushed updated site to origin.")
    else:
        print("Push skipped (use --push to push automatically).")

    return 0


if __name__ == "__main__":
    sys.exit(main())
