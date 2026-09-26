---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/resources
  - api/operation/create
  - api/effect/write
up: "[[MCP - Admin Control]]"
app: "Admin Control"
method: POST
path: "/admin/control/v1/orgs/{orgId}/policies/{policyId}/resources"
category: "Resources"
writes_data: true
---
# Admin Control - Create a new policy resource

**Create a new policy resource** — `POST /admin/control/v1/orgs/{orgId}/policies/{policyId}/resources`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Control - Create a new policy resource"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/control/rest/

```http
POST https://api.atlassian.com/admin/control/v1/orgs/{{service.org_id}}/policies/{{param:policyId}}/resources
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `policyId` (path, string, required) — Unique Id associated with each policy.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Add a new resource to a policy

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `write:policies:admin`
