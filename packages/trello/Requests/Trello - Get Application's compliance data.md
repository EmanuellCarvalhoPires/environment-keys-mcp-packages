---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/applications
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/applications/{key}/compliance"
category: "Applications"
writes_data: false
---
# Trello - Get Application's compliance data

**Get Application's compliance data** — `GET /applications/{key}/compliance`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Application's compliance data"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/applications/{{param:key}}/compliance
Authorization: {{service.auth_token}}
```

## Parameters

- `key` (path, string, required) — Value of key in the path.

