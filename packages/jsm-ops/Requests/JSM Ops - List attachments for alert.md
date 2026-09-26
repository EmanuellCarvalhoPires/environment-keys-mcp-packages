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
path: "/api/{cloudId}/v1/alerts/{alertId}/attachments"
category: "Alerts"
writes_data: false
---
# JSM Ops - List attachments for alert

**List attachments for alert** — `GET /api/{cloudId}/v1/alerts/{alertId}/attachments`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List attachments for alert"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:alertId}}/attachments?after={{param:after}}&size={{param:size}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `alertId` (path, string, required) — The ID of the alert.
- `after` (query, string, optional) — The pagination token for fetching the next page of results.
- `size` (query, string, optional) — The maximum number of items to return per page.

## Original description

Lists all attachments for the given alert with pagination support.
