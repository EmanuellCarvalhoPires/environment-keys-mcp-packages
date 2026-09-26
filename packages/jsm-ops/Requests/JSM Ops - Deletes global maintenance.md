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
path: "/api/{cloudId}/v1/maintenances/{id}"
category: "Maintenances"
writes_data: true
---
# JSM Ops - Deletes global maintenance

**Deletes global maintenance** — `DELETE /api/{cloudId}/v1/maintenances/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Deletes global maintenance"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/maintenances/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Identifier of the maintenance.

## Original description

This request is used to delete a global maintenance.
