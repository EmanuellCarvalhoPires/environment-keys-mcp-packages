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
path: "/stakeholder-comms/cloudId/{cloudId}/api/pages/summary"
category: "Status Page"
writes_data: false
---
# JSM Ops - Get pages summary by cloud ID

**Get pages summary by cloud ID** — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/summary`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get pages summary by cloud ID"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/pages/summary?filter={{param:filter}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `filter` (query, string, optional) — Filter pages by status.

## Original description

Get summary of all Status pages for a given cloud ID.
