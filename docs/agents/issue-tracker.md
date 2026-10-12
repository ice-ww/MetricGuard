# Issue tracker: GitHub

Issues and specs live in ice-ww/MetricGuard on GitHub.
Use the gh CLI from the repository directory.

- Create: gh issue create --title "..." --body-file <file>
- Read: gh issue view <number> --json number,title,body,labels,comments
- List: gh issue list --state open --json number,title,body,labels
- Comment: gh issue comment <number> --body-file <file>
- Label: gh issue edit <number> --add-label "..."
- Remove label: gh issue edit <number> --remove-label "..."
- Close: gh issue close <number>

Write multiline bodies to a UTF-8 file and use --body-file.
Use --repo ice-ww/MetricGuard when outside this repository.

“Publish to the issue tracker” means create a GitHub issue.
“Fetch the relevant ticket” means read its issue and comments.

Link child issues using GitHub sub-issues when available.
Otherwise, add “Part of #<parent>” to the child and a task
list in the parent. Record blockers using native dependencies
when available; otherwise use “Blocked by: #<number>”.

## Pull requests as a triage surface

PRs as a request surface: no.
