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
path: "/stakeholder-comms/cloudId/{cloudId}/api/subscribers/stats"
category: "Status Page"
writes_data: false
---
# JSM Ops - Get subscription stats

**Get subscription stats** — `GET /stakeholder-comms/cloudId/{cloudId}/api/subscribers/stats`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get subscription stats"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/subscribers/stats?itemId={{param:itemId}}&type={{param:type}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `itemId` (query, string, required) — Identifier of the item (page or incident).
- `type` (query, string, required) — Type of the item (PAGE or INCIDENT).

## Original description

Get subscription statistics for a status page item.
