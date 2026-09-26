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
path: "/stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/permanent_delete"
category: "Status Page"
writes_data: true
---
# JSM Ops - Permanently delete page

**Permanently delete page** — `POST /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/permanent_delete`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Permanently delete page"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/pages/{{param:pageId}}/permanent_delete
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `pageId` (path, string, required) — Identifier of the page.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Permanently delete a Stakeholder Comms page.
