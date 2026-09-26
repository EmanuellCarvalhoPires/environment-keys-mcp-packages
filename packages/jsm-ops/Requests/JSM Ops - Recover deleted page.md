---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/status-page
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/recover_deleted"
category: "Status Page"
writes_data: true
---
# JSM Ops - Recover deleted page

**Recover deleted page** — `POST /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/recover_deleted`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Recover deleted page"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/pages/{{param:pageId}}/recover_deleted
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `pageId` (path, string, required) — Identifier of the page.

## Original description

Recover a hard-deleted Status page.
