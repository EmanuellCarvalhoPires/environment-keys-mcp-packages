---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/policies
  - api/operation/get
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: GET
path: "/v1/orgs/{orgId}/policies/{policyId}"
category: "Policies"
writes_data: false
---
# Admin Orgs - Get a policy by ID

**Get a policy by ID** — `GET /v1/orgs/{orgId}/policies/{policyId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Get a policy by ID"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v1/orgs/{{service.org_id}}/policies/{{param:policyId}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `policyId` (path, string, required) — ID of the policy to query

## Original description

Returns information about a single policy by ID
