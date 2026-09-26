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
path: "/stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/with_memberships"
category: "Stakeholder User management"
writes_data: false
---
# JSM Ops - Get stakeholder groups with memberships

**Get stakeholder groups with memberships** — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/with_memberships`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get stakeholder groups with memberships"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/stakeholder_groups/with_memberships?first={{param:first}}&after={{param:after}}&last={{param:last}}&before={{param:before}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `first` (query, string, optional) — Number of items to return from the start.
- `after` (query, string, optional) — Cursor for forward pagination.
- `last` (query, string, optional) — Number of items to return from the end.
- `before` (query, string, optional) — Cursor for backward pagination.

## Original description

Get a paginated list of stakeholder groups with their members.
