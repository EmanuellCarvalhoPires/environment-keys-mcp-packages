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
path: "/admin/control/v2/orgs/{orgId}/policies/{policyId}/resources"
category: "Resources"
writes_data: true
---
# Admin Control - Delete all policy resources V2

**Delete all policy resources V2** — `DELETE /admin/control/v2/orgs/{orgId}/policies/{policyId}/resources`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Control - Delete all policy resources V2"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/control/rest/

```http
DELETE https://api.atlassian.com/admin/control/v2/orgs/{{service.org_id}}/policies/{{param:policyId}}/resources
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `policyId` (path, string, required) — Unique Id associated with each policy.

## Original description

Remove all resources from a policy.
