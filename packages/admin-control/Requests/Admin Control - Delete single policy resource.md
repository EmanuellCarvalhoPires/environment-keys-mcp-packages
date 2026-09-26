---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/resources
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Admin Control]]"
app: "Admin Control"
method: DELETE
path: "/admin/control/v1/orgs/{orgId}/policies/{policyId}/resources/{resourceId}"
category: "Resources"
writes_data: true
---
# Admin Control - Delete single policy resource

**Delete single policy resource** — `DELETE /admin/control/v1/orgs/{orgId}/policies/{policyId}/resources/{resourceId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Control - Delete single policy resource"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/control/rest/

```http
DELETE https://api.atlassian.com/admin/control/v1/orgs/{{service.org_id}}/policies/{{param:policyId}}/resources/{{param:resourceId}}
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `policyId` (path, string, required) — Unique Id associated with each policy.
- `resourceId` (path, string, required) — Unique Id associated with a resource.

## Original description

Delete one resource from a policy

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `write:policies:admin`
