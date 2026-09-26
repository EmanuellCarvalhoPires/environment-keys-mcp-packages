---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/policies
  - api/operation/create
  - api/effect/write
up: "[[MCP - Admin Control]]"
app: "Admin Control"
method: POST
path: "/admin/control/v1/orgs/{orgId}/policies"
category: "Policies"
writes_data: true
---
# Admin Control - Create a new policy

**Create a new policy** — `POST /admin/control/v1/orgs/{orgId}/policies`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Control - Create a new policy"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/control/rest/

```http
POST https://api.atlassian.com/admin/control/v1/orgs/{{service.org_id}}/policies
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create a policy aligned with your organization's standards.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `write:policies:admin`
