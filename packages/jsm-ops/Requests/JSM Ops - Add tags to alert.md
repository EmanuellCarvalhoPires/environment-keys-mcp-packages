---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/alerts
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/alerts/{id}/tags"
category: "Alerts"
writes_data: true
---
# JSM Ops - Add tags to alert

**Add tags to alert** — `POST /api/{cloudId}/v1/alerts/{id}/tags`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Add tags to alert"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:id}}/tags
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Identifier of the alert.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

This endpoint is used to add tags to an existing alert. Tags provide a means to categorize and manage alerts more effectively, enabling quick identification and sorting of related alerts based on the assigned tags.
