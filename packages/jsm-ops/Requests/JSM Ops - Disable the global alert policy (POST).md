---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/team-policies
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/teams/{teamId}/policies/{policyId}/disable"
category: "Team Policies"
writes_data: true
---
# JSM Ops - Disable the global alert policy (POST)

**Disable the global alert policy** — `POST /api/{cloudId}/v1/teams/{teamId}/policies/{policyId}/disable`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Disable the global alert policy (POST)"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/policies/{{param:policyId}}/disable
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `teamId` (path, string, required) — The jira team identifier
- `policyId` (path, string, required) — Identifier of the policy.

## Original description

Disable the global alert policy
