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
path: "/rest/agile/1.0/board/{boardId}/features"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_features_for_board]]"
---
# JSW - Get features for board

**Get features for board** — `GET /rest/agile/1.0/board/{boardId}/features`

- Run by the tool [[jsw_get_features_for_board]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/board/{{param:boardId}}/features
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `boardId` (path, string, required) — Value of boardId in the path.

