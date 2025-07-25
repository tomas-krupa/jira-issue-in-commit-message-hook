#!/usr/bin/env python3
import sys
import re
import argparse


JIRA_REGEX = re.compile(r"\b[A-Z][A-Z0-9]{1,9}-\d+\b")


def main():
    parser = argparse.ArgumentParser(description="Check commit message for JIRA key")
    parser.add_argument("commit_msg_path", help="Path to commit message file")
    parser.add_argument(
        "--exclude", help="Regex pattern to skip check if matched", default=None
    )
    args = parser.parse_args()

    try:
        with open(args.commit_msg_path, encoding="utf-8") as f:
            commit_msg = f.read()
    except Exception as e:
        print(f"ERROR: Failed to read commit message: {e}")
        return 1

    if commit_msg.startswith("Merge"):
        return 0

    if args.exclude and re.search(args.exclude, commit_msg):
        return 0

    if not JIRA_REGEX.search(commit_msg):
        print("ERROR: Commit message must contain a JIRA issue key (e.g., PROJ-1234).")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
