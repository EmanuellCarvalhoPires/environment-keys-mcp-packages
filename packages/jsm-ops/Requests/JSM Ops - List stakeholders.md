---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/stakeholder-user-management
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/stakeholder-comms/cloudId/{cloudId}/api/stakeholders/list"
category: "Stakeholder User management"
writes_data: false
---
# JSM Ops - List stakeholders

**List stakeholders** — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/list`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List stakeholders"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/stakeholders/list?status={{param:status}}&type={{param:type}}&searchField={{param:searchField}}&searchValue={{param:searchValue}}&orderBy={{param:orderBy}}&descending={{param:descending}}&first={{param:first}}&after={{param:after}}&last={{param:last}}&before={{param:before}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `status` (query, string, optional) — Filter by stakeholder status.
- `type` (query, string, optional) — Filter by stakeholder type.
- `searchField` (query, string, optional) — Field to search on.
- `searchValue` (query, string, optional) — Value to search for.
- `orderBy` (query, string, optional) — Field to order results by.
- `descending` (query, string, optional) — Order results in descending order.
- `first` (query, string, optional) — Number of items to return from the start.
- `after` (query, string, optional) — Cursor for forward pagination.
- `last` (query, string, optional) — Number of items to return from the end.
- `before` (query, string, optional) — Cursor for backward pagination.

## Original description

Get a list of stakeholders.
