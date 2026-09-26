---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/audit-logs
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/logs"
category: "Audit Logs"
writes_data: false
---
# JSM Ops - Get audit Logs

**Get audit Logs** — `GET /api/{cloudId}/v1/logs`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get audit Logs"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/logs?limit={{param:limit}}&pageToken={{param:pageToken}}&category={{param:category}}&level={{param:level}}&startTime={{param:startTime}}&endTime={{param:endTime}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `limit` (query, string, optional) — Maximum number of items to return in the response.
- `pageToken` (query, string, optional) — Token for fetching the next set of paginated results. The page token can be retrieved from the links.next key in each API response.
- `category` (query, string, optional) — Filter the audit logs based on the event category. Multiple categories can be passed by providing a comma-separated list of values.
- `level` (query, string, optional) — Filter the audit logs based on the log level. Multiple log levels can be passed by providing a comma-separated list of values.
- `startTime` (query, string, required) — The starting date-time after which returned audit logs must have been created. Accepts the ISO format (yyyy-MM-dd'T'HH:mm:ssZ) (e.g. 2024-01-15T08:00:00+02:00).
- `endTime` (query, string, required) — The ending date-time before which returned audit logs must have been created. Accepts the ISO format (yyyy-MM-dd'T'HH:mm:ssZ) (e.g. 2024-01-15T08:00:00+02:00).

## Original description

This endpoint returns all operations audit logs in Jira Service Management, allowing retrieval of logs in a specified time range and  filtering based on log level and category.   **Permissions required:** Permission to view Jira Service Management Audit logs using a JSM Org/Site/Product admin role
