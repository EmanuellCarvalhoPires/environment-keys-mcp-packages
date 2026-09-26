---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/alerts
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/alerts/{id}/logs"
category: "Alerts"
writes_data: false
---
# JSM Ops - List alert logs

**List alert logs** — `GET /api/{cloudId}/v1/alerts/{id}/logs`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List alert logs"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:id}}/logs?after={{param:after}}&size={{param:size}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Identifier of the alert.
- `after` (query, string, optional) — This parameter is used in pagination for the alert logs retrieved by the system. It accepts a string key of the last record from the previous page.
- `size` (query, string, optional) — This parameter is used to limit the number of alert logs returned by the system. It accepts an integer that specifies the maximum number of logs to be retrieved.

## Original description

This endpoint is used to retrieve a paginated list of alert logs which provides users to obtain a comprehensive record of alert activities. This includes alert creation, acknowledgment, assignment, and closure details. This endpoint is crucial for audit purposes, incident reviews, and enhancing the overall incident management process by providing complete visibility into alert history.
