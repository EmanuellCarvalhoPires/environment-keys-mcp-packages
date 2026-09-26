---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/policies
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: PUT
path: "/api/{cloudId}/v1/alerts/policies/{policyId}"
category: "Policies"
writes_data: true
---
# JSM Ops - Put global alert policy

**Put global alert policy** — `PUT /api/{cloudId}/v1/alerts/policies/{policyId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Put global alert policy"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PUT https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/policies/{{param:policyId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `policyId` (path, string, required) — Identifier of the policy.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Put global alert policy
