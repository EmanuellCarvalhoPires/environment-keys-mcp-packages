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
path: "/stakeholder-comms/cloudId/{cloudId}/api/subscribers/delete"
category: "Status Page"
writes_data: true
---
# JSM Ops - Delete subscribers

**Delete subscribers** — `POST /stakeholder-comms/cloudId/{cloudId}/api/subscribers/delete`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete subscribers"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/subscribers/delete
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Delete one or more subscribers from status page.
