---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/alerts
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/alerts/requests/{id}"
category: "Alerts"
writes_data: false
---
# JSM Ops - Get request status

**Get request status** — `GET /api/{cloudId}/v1/alerts/requests/{id}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get request status"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/requests/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Identifier of the questioned request. Please note that ID of the request was provided within response.

## Original description

Alert creation, deletion, and action requests are processed asynchronously to provide higher availability and scalability. This endpoint is used to track the status and alert details (if any) of the request whose identifier is given.
