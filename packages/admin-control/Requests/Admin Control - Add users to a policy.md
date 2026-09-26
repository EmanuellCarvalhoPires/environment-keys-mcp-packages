---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/authentication-policies
  - api/operation/create
  - api/effect/write
up: "[[MCP - Admin Control]]"
app: "Admin Control"
method: POST
path: "/admin/control/v1/orgs/{orgId}/auth-policy/{policyId}/add-users"
category: "Authentication Policies"
writes_data: true
---
# Admin Control - Add users to a policy

**Add users to a policy** — `POST /admin/control/v1/orgs/{orgId}/auth-policy/{policyId}/add-users`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Control - Add users to a policy"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/control/rest/

```http
POST https://api.atlassian.com/admin/control/v1/orgs/{{service.org_id}}/auth-policy/{{param:policyId}}/add-users
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `policyId` (path, string, required) — Unique Id associated with each policy.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Add users to an authentication policy to address the security of different user sets. [Understand how to add users to a policy and check the status](https://developer.atlassian.com/cloud/admin/auth-policy-cookbook/)

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `write:policies:admin`
