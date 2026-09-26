---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/agile/1.0/board/{boardId}/reports"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_reports_for_board]]"
---
# JSW - Get reports for board

**Get reports for board** — `GET /rest/agile/1.0/board/{boardId}/reports`

- Run by the tool [[jsw_get_reports_for_board]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/board/{{param:boardId}}/reports
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `boardId` (path, string, required) — Value of boardId in the path.

