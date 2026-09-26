---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/team-policies
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/teams/{teamId}/policies/{policyId}"
category: "Team Policies"
writes_data: false
---
# JSM Ops - Get team policy

**Get team policy** — `GET /api/{cloudId}/v1/teams/{teamId}/policies/{policyId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get team policy"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/policies/{{param:policyId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `teamId` (path, string, required) — The jira team identifier
- `policyId` (path, string, required) — Identifier of the policy.

## Original description

Get team policy
