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
path: "/stakeholder-comms/cloudId/{cloudId}/api/incidents/list/v2"
category: "Status Page"
writes_data: false
---
# JSM Ops - List incidents with pagination

**List incidents with pagination** — `GET /stakeholder-comms/cloudId/{cloudId}/api/incidents/list/v2`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List incidents with pagination"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/incidents/list/v2?pageId={{param:pageId}}&showActive={{param:showActive}}&first={{param:first}}&after={{param:after}}&last={{param:last}}&before={{param:before}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `pageId` (query, string, optional) — Identifier of the page to filter incidents.
- `showActive` (query, string, optional) — Filter to show only active incidents.
- `first` (query, string, optional) — Number of items to return from the start.
- `after` (query, string, optional) — Cursor for forward pagination.
- `last` (query, string, optional) — Number of items to return from the end.
- `before` (query, string, optional) — Cursor for backward pagination.

## Original description

Get a paginated list of incidents managed through stakeholder communication.
