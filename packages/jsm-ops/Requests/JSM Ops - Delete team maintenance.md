---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/maintenances
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/teams/{teamId}/maintenances/{id}"
category: "Maintenances"
writes_data: true
---
# JSM Ops - Delete team maintenance

**Delete team maintenance** — `DELETE /api/{cloudId}/v1/teams/{teamId}/maintenances/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete team maintenance"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/maintenances/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `teamId` (path, string, required) — Identifier of the maintenance owning team.
- `id` (path, string, required) — Identifier of the maintenance.

## Original description

Deletes a maintenance with given id in the request.
