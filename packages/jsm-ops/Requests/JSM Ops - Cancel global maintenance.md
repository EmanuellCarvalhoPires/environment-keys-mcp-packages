---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/maintenances
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/maintenances/{id}/cancel"
category: "Maintenances"
writes_data: true
---
# JSM Ops - Cancel global maintenance

**Cancel global maintenance** — `POST /api/{cloudId}/v1/maintenances/{id}/cancel`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Cancel global maintenance"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/maintenances/{{param:id}}/cancel
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Identifier of the maintenance.

## Original description

This endpoint is used to stop an ongoing maintenance plan early. The functionality allows you to end the maintenance plan before the initially set end time.
