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
path: "/stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/summary"
category: "Status Page"
writes_data: false
---
# JSM Ops - Get page summary details

**Get page summary details** — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/summary`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get page summary details"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/pages/{{param:pageId}}/summary
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `pageId` (path, string, required) — Identifier of the page.

## Original description

Get summary details for a status page, its components and system health.
