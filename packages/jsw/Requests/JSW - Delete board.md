---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSW]]"
app: "JSW"
method: DELETE
path: "/rest/agile/1.0/board/{boardId}"
category: "Board"
writes_data: true
tool_note: "[[jsw_delete_board]]"
---
# JSW - Delete board

**Delete board** — `DELETE /rest/agile/1.0/board/{boardId}`

- Run by the tool [[jsw_delete_board]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/agile/1.0/board/{{param:boardId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `boardId` (path, string, required) — ID of the board to be deleted

## Original description

Deletes the board. Admin without the view permission can still remove the board.
