---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/users
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: POST
path: "/v1/orgs/{orgId}/users/{userId}/role-assignments/assign"
category: "Users"
writes_data: true
---
# Admin Orgs - Assign organization-level role

**Assign organization-level role** — `POST /v1/orgs/{orgId}/users/{userId}/role-assignments/assign`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Orgs - Assign organization-level role"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
POST https://api.atlassian.com/admin/v1/orgs/{{service.org_id}}/users/{{param:userId}}/role-assignments/assign
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `userId` (path, string, required) — Every user has a unique ID. Find a user’s account ID by using the Get users endpoint.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Assign an organization-level role to a user. These are roles that have organization-wide privileges, like organization admin.

This operation follows eventual consistency. Changes may take up to 30 seconds to be reflected after the operation is performed.
