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
path: "/stakeholder-comms/cloudId/{cloudId}/api/subscribers/list"
category: "Status Page"
writes_data: false
---
# JSM Ops - List subscribers

**List subscribers** — `GET /stakeholder-comms/cloudId/{cloudId}/api/subscribers/list`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List subscribers"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/subscribers/list?itemType={{param:itemType}}&itemId={{param:itemId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `itemType` (query, string, required) — Type of the item to list subscribers for (page or incident).
- `itemId` (query, string, required) — Identifier of the item to list subscribers for.

## Original description

Get a list of subscribers for a status page item.
