#!/usr/bin/env python3

import argparse
import subprocess
import sys
from datetime import datetime


def run(cmd: list[str]) -> None:
    result = subprocess.run(cmd)
    if result.returncode != 0:
        sys.exit(result.returncode)


def current_branch() -> str:
    result = subprocess.run(
        ["git", "branch", "--show-current"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def ensure_clean_worktree() -> None:
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True,
        check=True,
    )
    if result.stdout.strip():
        print("Working tree not clean. Commit or stash changes first.")
        sys.exit(1)


def create_branch(name: str, base: str) -> None:
    ensure_clean_worktree()
    run(["git", "checkout", base])
    run(["git", "pull"])
    run(["git", "checkout", "-b", name])
    print(f"Created and switched to branch '{name}' from '{base}'")


def commit(message: str, add_all: bool, prefix: str | None) -> None:
    if add_all:
        run(["git", "add", "-A"])

    if prefix:
        message = f"{prefix}: {message}"

    run(["git", "commit", "-m", message])
    print(f"Committed with message: {message}")


def push(set_upstream: bool) -> None:
    branch = current_branch()
    if set_upstream:
        run(["git", "push", "-u", "origin", branch])
    else:
        run(["git", "push"])
    print(f"Pushed branch '{branch}'")


def squash_merge(target: str) -> None:
    branch = current_branch()
    if branch == target:
        print("Cannot squash merge into the same branch.")
        sys.exit(1)

    ensure_clean_worktree()

    run(["git", "checkout", target])
    run(["git", "pull"])
    run(["git", "merge", "--squash", branch])

    timestamp = datetime.now().strftime("%Y-%m-%d")
    message = f"merge({branch}): squash merge on {timestamp}"
    run(["git", "commit", "-m", message])

    print(f"Squash merged '{branch}' into '{target}'")


def main():
    parser = argparse.ArgumentParser(
        prog="zensical-git", description="Common Git workflow automation"
    )

    sub = parser.add_subparsers(dest="command", required=True)

    # branch
    branch_parser = sub.add_parser("branch", help="Create new branch from base")
    branch_parser.add_argument("name", help="Branch name")
    branch_parser.add_argument(
        "--base", default="main", help="Base branch (default: main)"
    )

    # commit
    commit_parser = sub.add_parser("commit", help="Commit changes")
    commit_parser.add_argument("message", help="Commit message")
    commit_parser.add_argument("--all", action="store_true", help="Stage all changes")
    commit_parser.add_argument(
        "--type",
        choices=["feat", "fix", "chore", "refactor", "test", "docs"],
        help="Conventional commit type",
    )

    # push
    push_parser = sub.add_parser("push", help="Push current branch")
    push_parser.add_argument("--set-upstream", action="store_true")

    # squash
    squash_parser = sub.add_parser("squash", help="Squash merge into target branch")
    squash_parser.add_argument("target", help="Target branch")

    args = parser.parse_args()

    if args.command == "branch":
        create_branch(args.name, args.base)

    elif args.command == "commit":
        commit(args.message, args.all, args.type)

    elif args.command == "push":
        push(args.set_upstream)

    elif args.command == "squash":
        squash_merge(args.target)


if __name__ == "__main__":
    main()
