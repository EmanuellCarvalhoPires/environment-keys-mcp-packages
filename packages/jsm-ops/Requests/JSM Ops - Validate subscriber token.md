---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/status-page
  - api/operation/search
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/stakeholder-comms/cloudId/{cloudId}/api/subscribers/validate_token"
category: "Status Page"
writes_data: false
---
# JSM Ops - Validate subscriber token

**Validate subscriber token** — `POST /stakeholder-comms/cloudId/{cloudId}/api/subscribers/validate_token`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Validate subscriber token"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/subscribers/validate_token
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Validate a subscriber token in Status page.
