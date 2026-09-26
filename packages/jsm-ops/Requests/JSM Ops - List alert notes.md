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
path: "/api/{cloudId}/v1/alerts/{id}/notes"
category: "Alerts"
writes_data: false
---
# JSM Ops - List alert notes

**List alert notes** — `GET /api/{cloudId}/v1/alerts/{id}/notes`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List alert notes"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:id}}/notes?after={{param:after}}&size={{param:size}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Identifier of the alert.
- `after` (query, string, optional) — This parameter is used in pagination for the alert notes. It accepts a string key of the last record from the previous page.
- `size` (query, string, optional) — This parameter is used to limit the number of alert notes returned by the system. It accepts an integer that specifies the maximum number of notes to be retrieved.

## Original description

This endpoint is used to retrieve a list of notes for a specified alert. Notes provide additional information or context about an alert, helping to enhance the understanding and management of alerts.
