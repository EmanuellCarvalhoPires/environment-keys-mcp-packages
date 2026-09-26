---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/policies
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/alerts/policies/{policyId}"
category: "Policies"
writes_data: false
---
# JSM Ops - Get global alert policy

**Get global alert policy** — `GET /api/{cloudId}/v1/alerts/policies/{policyId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get global alert policy"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/policies/{{param:policyId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `policyId` (path, string, required) — Identifier of the policy.

## Original description

Get global alert policy
