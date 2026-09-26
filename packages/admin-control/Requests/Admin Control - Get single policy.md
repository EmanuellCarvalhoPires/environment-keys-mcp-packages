---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/policies
  - api/operation/get
  - api/effect/read
up: "[[MCP - Admin Control]]"
app: "Admin Control"
method: GET
path: "/admin/control/v1/orgs/{orgId}/policies/{policyId}"
category: "Policies"
writes_data: false
---
# Admin Control - Get single policy

**Get single policy** — `GET /admin/control/v1/orgs/{orgId}/policies/{policyId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Control - Get single policy"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/control/rest/

```http
GET https://api.atlassian.com/admin/control/v1/orgs/{{service.org_id}}/policies/{{param:policyId}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `policyId` (path, string, required) — Unique Id associated with each policy.

## Original description

Returns information about a policy by policyId.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:policies:admin`
