---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/alerts
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/alerts/{id}/acknowledge"
category: "Alerts"
writes_data: true
---
# JSM Ops - Acknowledge alert

**Acknowledge alert** — `POST /api/{cloudId}/v1/alerts/{id}/acknowledge`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Acknowledge alert"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:id}}/acknowledge
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Identifier of the alert.

## Original description

This endpoint is used to acknowledge an existing alert. Acknowledging an alert indicates that it has been received and is being acted upon, preventing duplicate efforts and coordinating response actions.
