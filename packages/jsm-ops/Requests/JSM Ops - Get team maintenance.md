---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/maintenances
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/teams/{teamId}/maintenances/{id}"
category: "Maintenances"
writes_data: false
---
# JSM Ops - Get team maintenance

**Get team maintenance** — `GET /api/{cloudId}/v1/teams/{teamId}/maintenances/{id}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get team maintenance"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/maintenances/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `teamId` (path, string, required) — Identifier of the maintenance owning team.
- `id` (path, string, required) — Identifier of the maintenance.

## Original description

This request is used to retrieve a specific maintenance of a specific team.
