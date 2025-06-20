#!/usr/bin/env python3
import sys
import re

# Default pattern: uppercase project key, dash, digits (e.g., ABC-123)
JIRA_REGEX = re.compile(r"\b[A-Z][A-Z0-9]{1,9}-\d+\b")


def main():
    if len(sys.argv) != 2:
        print("Usage: check_jira_commit.py <commit-msg-file>")
        return 1

    commit_msg_path = sys.argv[1]

    with open(commit_msg_path, encoding="utf-8") as f:
        commit_msg = f.read()

    if not JIRA_REGEX.search(commit_msg):
        print("❌ Commit message must contain a JIRA issue key (e.g., PROJ-1234).")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
