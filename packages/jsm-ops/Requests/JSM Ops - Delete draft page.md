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
path: "/stakeholder-comms/cloudId/{cloudId}/api/pages/draft/{draftPageId}/delete"
category: "Status Page"
writes_data: true
---
# JSM Ops - Delete draft page

**Delete draft page** — `POST /stakeholder-comms/cloudId/{cloudId}/api/pages/draft/{draftPageId}/delete`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete draft page"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/pages/draft/{{param:draftPageId}}/delete
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `draftPageId` (path, string, required) — Identifier of the draft page.

## Original description

Delete a draft Status page.
