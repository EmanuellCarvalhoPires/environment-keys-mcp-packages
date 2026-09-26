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
path: "/api/{cloudId}/v1/alerts/{id}/action"
category: "Alerts"
writes_data: true
---
# JSM Ops - Execute custom action

**Execute custom action** — `POST /api/{cloudId}/v1/alerts/{id}/action`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Execute custom action"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:id}}/action
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

This endpoint is used to execute custom actions on an existing alert. Custom actions allow for more flexible and specific responses to alerts, including integrations with external systems or triggering complex workflows. This operation is a powerful tool for extending the capabilities of the alert management process beyond predefined actions.
