---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/team-policies
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/teams/{teamId}/policies/{policyId}"
category: "Team Policies"
writes_data: true
---
# JSM Ops - Delete global alert policy (DELETE)

**Delete global alert policy** — `DELETE /api/{cloudId}/v1/teams/{teamId}/policies/{policyId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete global alert policy (DELETE)"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/policies/{{param:policyId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `teamId` (path, string, required) — The jira team identifier
- `policyId` (path, string, required) — Identifier of the policy.

## Original description

Delete global alert policy
