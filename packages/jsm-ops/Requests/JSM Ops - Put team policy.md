---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/team-policies
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: PUT
path: "/api/{cloudId}/v1/teams/{teamId}/policies/{policyId}"
category: "Team Policies"
writes_data: true
---
# JSM Ops - Put team policy

**Put team policy** — `PUT /api/{cloudId}/v1/teams/{teamId}/policies/{policyId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Put team policy"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PUT https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/policies/{{param:policyId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `teamId` (path, string, required) — The jira team identifier
- `policyId` (path, string, required) — Identifier of the policy.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Put team policy
