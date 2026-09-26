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
path: "/rest/agile/1.0/backlog/{boardId}/issue"
category: "Backlog"
writes_data: true
tool_note: "[[jsw_move_issues_to_backlog_for_board]]"
---
# JSW - Move issues to backlog for board

**Move issues to backlog for board** — `POST /rest/agile/1.0/backlog/{boardId}/issue`

- Run by the tool [[jsw_move_issues_to_backlog_for_board]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/agile/1.0/backlog/{{param:boardId}}/issue
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `boardId` (path, string, required) — Value of boardId in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "issues": [
    "PR-1",
    "10001",
    "PR-3"
  ],
  "rankBeforeIssue": "PR-4",
  "rankCustomFieldId": 10521
}
```

## Original description

Move issues to the backlog of a particular board (if they are already on that board).  
This operation is equivalent to remove future and active sprints from a given set of issues if the board has sprints If the board does not have sprints this will put the issues back into the backlog from the board. At most 50 issues may be moved at once.
