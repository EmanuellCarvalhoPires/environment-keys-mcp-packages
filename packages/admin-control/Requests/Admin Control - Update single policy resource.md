---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/resources
  - api/operation/update
  - api/effect/write
up: "[[MCP - Admin Control]]"
app: "Admin Control"
method: PUT
path: "/admin/control/v1/orgs/{orgId}/policies/{policyId}/resources/{resourceId}"
category: "Resources"
writes_data: true
---
# Admin Control - Update single policy resource

**Update single policy resource** — `PUT /admin/control/v1/orgs/{orgId}/policies/{policyId}/resources/{resourceId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Control - Update single policy resource"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/control/rest/

```http
PUT https://api.atlassian.com/admin/control/v1/orgs/{{service.org_id}}/policies/{{param:policyId}}/resources/{{param:resourceId}}
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `policyId` (path, string, required) — Unique Id associated with each policy.
- `resourceId` (path, string, required) — Unique Id associated with a resource.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Delete one resource from a policy

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `write:policies:admin`
