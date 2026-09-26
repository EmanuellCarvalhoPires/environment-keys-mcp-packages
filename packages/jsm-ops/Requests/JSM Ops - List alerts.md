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
path: "/api/{cloudId}/v1/alerts"
category: "Alerts"
writes_data: false
---
# JSM Ops - List alerts

**List alerts** — `GET /api/{cloudId}/v1/alerts`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List alerts"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts?size={{param:size}}&sort={{param:sort}}&offset={{param:offset}}&order={{param:order}}&query={{param:query}}&from={{param:from}}&to={{param:to}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `size` (query, string, optional) — Maximum number of items to provide in the result.
- `sort` (query, string, optional) — Name of the field that result set will be sorted by.
- `offset` (query, string, optional) — The offset parameter controls the starting point within the collection of resource results.
- `order` (query, string, optional) — Sorting order of the result set.
- `query` (query, string, optional) — This parameter is used to filter the alerts based on specified criteria. It accepts a string value that represents the search query.
- `from` (query, string, optional) — The starting date-time to consider while filtering the alerts. It helps in narrowing down the list of alerts to a specific time frame.
- `to` (query, string, optional) — The ending date-time to consider while filtering the alerts. Used in conjunction with 'from', it defines the specific time window to focus on for the alert listing.

## Original description

This endpoint is designed to provide a comprehensive view of all alerts in your system. This API supports pagination and filtering with allowing you to customize the view based on your specific needs. More than 20000 alerts cannot be retrieved. Sum of offset and size should be lower than 20K.
