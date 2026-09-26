---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/backlog
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSW]]"
app: "JSW"
method: POST
path: "/rest/agile/1.0/backlog/issue"
category: "Backlog"
writes_data: true
tool_note: "[[jsw_move_issues_to_backlog]]"
---
# JSW - Move issues to backlog

**Move issues to backlog** — `POST /rest/agile/1.0/backlog/issue`

- Run by the tool [[jsw_move_issues_to_backlog]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/agile/1.0/backlog/issue
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "issues": [
    "10001",
    "PR-1",
    "PR-3"
  ]
}
```

## Original description

Move issues to the backlog.  
This operation is equivalent to remove future and active sprints from a given set of issues. At most 50 issues may be moved at once.
