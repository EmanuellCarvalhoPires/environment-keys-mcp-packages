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
path: "/stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/components/uptime/v2"
category: "Status Page"
writes_data: false
---
# JSM Ops - Get components uptime for page with pagination

**Get components uptime for page with pagination** — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/components/uptime/v2`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get components uptime for page with pagination"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/pages/{{param:pageId}}/components/uptime/v2?startDate={{param:startDate}}&endDate={{param:endDate}}&searchTerm={{param:searchTerm}}&statusFilter={{param:statusFilter}}&first={{param:first}}&after={{param:after}}&last={{param:last}}&before={{param:before}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `pageId` (path, string, required) — Identifier of the page.
- `startDate` (query, string, optional) — Start of the period.
- `endDate` (query, string, optional) — End of the period.
- `searchTerm` (query, string, optional) — Search term to filter components.
- `statusFilter` (query, string, optional) — Filter components by status.
- `first` (query, string, optional) — Number of items to return from the start.
- `after` (query, string, optional) — Cursor for forward pagination.
- `last` (query, string, optional) — Number of items to return from the end.
- `before` (query, string, optional) — Cursor for backward pagination.

## Original description

Get uptime information for components associated with a Status page with pagination support.
