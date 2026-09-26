---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/policies
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/alerts/policies/{policyId}"
category: "Policies"
writes_data: true
---
# JSM Ops - Delete global alert policy

**Delete global alert policy** — `DELETE /api/{cloudId}/v1/alerts/policies/{policyId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete global alert policy"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/policies/{{param:policyId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `policyId` (path, string, required) — Identifier of the policy.

## Original description

Delete global alert policy
