---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/status-page
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/stakeholder-comms/cloudId/{cloudId}/api/subscribers"
category: "Status Page"
writes_data: true
---
# JSM Ops - Create subscriber

**Create subscriber** — `POST /stakeholder-comms/cloudId/{cloudId}/api/subscribers`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Create subscriber"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/subscribers
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Add a new subscriber for status page.
