---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/policies
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Admin Control]]"
app: "Admin Control"
method: DELETE
path: "/admin/control/v1/orgs/{orgId}/policies/{policyId}"
category: "Policies"
writes_data: true
---
# Admin Control - Delete single policy

**Delete single policy** — `DELETE /admin/control/v1/orgs/{orgId}/policies/{policyId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Control - Delete single policy"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/control/rest/

```http
DELETE https://api.atlassian.com/admin/control/v1/orgs/{{service.org_id}}/policies/{{param:policyId}}
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `policyId` (path, string, required) — Unique Id associated with each policy.

## Original description

Delete a policy with a policyId

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `delete:policies:admin`
