# jira-issue-in-commit-message-hook

A simple yet powerful `pre-commit` hook that ensures all commit messages include a valid JIRA issue key (e.g., `PROJ-123`). This helps enforce traceability and integrates nicely with team workflows that use JIRA.

## Installation

1. Add this repository to your `.pre-commit-config.yaml`:

   ```yaml
   - repo: https://github.com/tomas-krupa/jira-issue-in-commit-message-hook.git
     rev: 1.0.0
     hooks:
       - id: jira-issue-in-commit-message
       stages: [commit-msg]
   ```

2. Install the pre-commit hooks:

   ```bash
   pre-commit install
   ```

3. Make a commit with to see the hook in action.

   ```bash
   $ git commit -m "this commmit message is missing JIRA issue" --allow-empty
   jira-issue-in-commit-message.............................................Failed
   - hook id: jira-issue-in-commit-message
   - exit code: 1

   ERROR: Commit message must contain a JIRA issue key (e.g., PROJ-1234).

   $ git commit -m "this commmit message is correct [PROJECT-12345]" --allow-empty
   jira-issue-in-commit-message.............................................Passed
   [feature/pre-commit 093cfb7b] this commmit message is correct [PROJECT-12345]
   ```

## CI/CD integration

To enforce a consistent commit message format within your CI/CD pipeline using this pre-commit hook, you can integrate the following command into your build job:

   ```bash
   # Prerequisite: The pre-commit hook must be installed
   git commit --amend --no-edit   # This triggers the commit message check
   git reset --hard ORIG_HEAD     # This restores the original state prior to the amend
   ```
