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
path: "/api/{cloudId}/v1/alerts/{id}/escalate"
category: "Alerts"
writes_data: true
---
# JSM Ops - Escalate alert to next

**Escalate alert to next** — `POST /api/{cloudId}/v1/alerts/{id}/escalate`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Escalate alert to next"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:id}}/escalate
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Identifier of the alert.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

This endpoint is used to escalate an existing alert. Escalation triggers the defined escalation policies which could involve notifying additional users or teams, or increasing the frequency of notifications for the alert. This operation is particularly useful in situations where an alert requires urgent attention or has not been addressed within a certain timeframe according to the pre-set escalation paths.
