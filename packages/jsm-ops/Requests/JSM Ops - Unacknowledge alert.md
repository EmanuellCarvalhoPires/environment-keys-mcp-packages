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
path: "/api/{cloudId}/v1/alerts/{id}/unacknowledge"
category: "Alerts"
writes_data: true
---
# JSM Ops - Unacknowledge alert

**Unacknowledge alert** — `POST /api/{cloudId}/v1/alerts/{id}/unacknowledge`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Unacknowledge alert"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:id}}/unacknowledge
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Identifier of the alert.

## Original description

This endpoint is used to set the 'acknowledged' property of an existing alert as 'false', effectively marking it's status as 'open'. This allows for better tracking and management of alerts by indicating that an alert has not yet been acknowledged or addressed.
