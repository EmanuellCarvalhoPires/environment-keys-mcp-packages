---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSW]]"
app: "JSW"
method: PUT
path: "/rest/agile/1.0/board/{boardId}/features"
category: "Board"
writes_data: true
tool_note: "[[jsw_toggle_features]]"
---
# JSW - Toggle features

**Toggle features** — `PUT /rest/agile/1.0/board/{boardId}/features`

- Run by the tool [[jsw_toggle_features]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
PUT {{service.url}}/rest/agile/1.0/board/{{param:boardId}}/features
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `boardId` (path, string, required) — Value of boardId in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

