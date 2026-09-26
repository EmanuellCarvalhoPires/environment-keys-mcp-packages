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
path: "/api/{cloudId}/v1/teams/{teamId}/policies/{policyId}/change-order"
category: "Team Policies"
writes_data: true
---
# JSM Ops - Change the order of team policy

**Change the order of team policy** — `POST /api/{cloudId}/v1/teams/{teamId}/policies/{policyId}/change-order`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Change the order of team policy"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/policies/{{param:policyId}}/change-order
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `teamId` (path, string, required) — The jira team identifier
- `policyId` (path, string, required) — Identifier of the policy.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Change the order of team policy
