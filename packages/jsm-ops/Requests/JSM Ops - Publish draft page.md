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
path: "/stakeholder-comms/cloudId/{cloudId}/api/pages/draft/{draftPageId}/publish"
category: "Status Page"
writes_data: true
---
# JSM Ops - Publish draft page

**Publish draft page** — `POST /stakeholder-comms/cloudId/{cloudId}/api/pages/draft/{draftPageId}/publish`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Publish draft page"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/pages/draft/{{param:draftPageId}}/publish
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `draftPageId` (path, string, required) — Identifier of the draft page to publish.

## Original description

Publish a draft Status page.
