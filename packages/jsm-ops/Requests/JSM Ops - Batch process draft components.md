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
path: "/stakeholder-comms/cloudId/{cloudId}/api/components/batch_process"
category: "Status Page"
writes_data: true
---
# JSM Ops - Batch process draft components

**Batch process draft components** — `POST /stakeholder-comms/cloudId/{cloudId}/api/components/batch_process`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Batch process draft components"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/components/batch_process
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create, update, or delete draft components for a Status page in a single batch operation.
