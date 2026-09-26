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
path: "/stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/components/draft"
category: "Status Page"
writes_data: false
---
# JSM Ops - List components in draft for a status page

**List components in draft for a status page.** — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/components/draft`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List components in draft for a status page"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/pages/{{param:pageId}}/components/draft
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `pageId` (path, string, required) — Identifier of the page.

## Original description

List components in draft for a status page.
