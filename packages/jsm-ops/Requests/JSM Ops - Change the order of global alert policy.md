---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/policies
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/alerts/policies/{policyId}/change-order"
category: "Policies"
writes_data: true
---
# JSM Ops - Change the order of global alert policy

**Change the order of global alert policy** — `POST /api/{cloudId}/v1/alerts/policies/{policyId}/change-order`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Change the order of global alert policy"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/policies/{{param:policyId}}/change-order
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `policyId` (path, string, required) — Value of policyId in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Change the order of global alert policy
