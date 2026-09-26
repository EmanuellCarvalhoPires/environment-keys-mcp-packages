---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSW]]"
app: "JSW"
method: POST
path: "/rest/agile/1.0/board/{boardId}/issue"
category: "Board"
writes_data: true
tool_note: "[[jsw_move_issues_to_board]]"
---
# JSW - Move issues to board

**Move issues to board** — `POST /rest/agile/1.0/board/{boardId}/issue`

- Run by the tool [[jsw_move_issues_to_board]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/agile/1.0/board/{{param:boardId}}/issue
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

Move issues from the backog to the board (if they are already in the backlog of that board).  
This operation either moves an issue(s) onto a board from the backlog (by adding it to the issueList for the board) Or transitions the issue(s) to the first column for a kanban board with backlog. At most 50 issues may be moved at once.
