---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/policies
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin Control]]"
app: "Admin Control"
method: GET
path: "/admin/control/v1/orgs/{orgId}/policies/{policyId}/validate"
category: "Policies"
writes_data: false
---
# Admin Control - Validate a policy

**Validate a policy** — `GET /admin/control/v1/orgs/{orgId}/policies/{policyId}/validate`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Control - Validate a policy"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/control/rest/

```http
GET https://api.atlassian.com/admin/control/v1/orgs/{{service.org_id}}/policies/{{param:policyId}}/validate
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `policyId` (path, string, required) — Unique Id associated with each policy.

## Original description

Validate a policy to view potential issues in your policy

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:policies:admin`
