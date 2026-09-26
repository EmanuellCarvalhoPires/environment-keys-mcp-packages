---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/status-page
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/stakeholder-comms/cloudId/{cloudId}/api/subscribers/list/connection"
category: "Status Page"
writes_data: false
---
# JSM Ops - List subscribers with pagination and filters

**List subscribers with pagination and filters** — `GET /stakeholder-comms/cloudId/{cloudId}/api/subscribers/list/connection`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List subscribers with pagination and filters"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/subscribers/list/connection?pageId={{param:pageId}}&cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `pageId` (query, string, optional) — Filter subscribers by page identifier.
- `cursor` (query, string, optional) — Cursor for pagination.
- `limit` (query, string, optional) — Maximum number of subscribers to return.

## Original description

Get paginated list of subscribers with advanced filtering options.
