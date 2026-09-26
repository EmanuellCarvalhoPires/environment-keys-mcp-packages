---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/resources
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin Control]]"
app: "Admin Control"
method: GET
path: "/admin/control/v1/orgs/{orgId}/policies/{policyId}/resources"
category: "Resources"
writes_data: false
---
# Admin Control - Get list of resources associated with a policy

**Get list of resources associated with a policy** — `GET /admin/control/v1/orgs/{orgId}/policies/{policyId}/resources`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Control - Get list of resources associated with a policy"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/control/rest/

```http
GET https://api.atlassian.com/admin/control/v1/orgs/{{service.org_id}}/policies/{{param:policyId}}/resources
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `policyId` (path, string, required) — Unique Id associated with each policy.

## Original description

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:policies:admin`
