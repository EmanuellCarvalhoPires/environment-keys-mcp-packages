---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/users
  - api/operation/action
  - api/effect/write
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: POST
path: "/v1/orgs/{orgId}/users/{userId}/roles/assign"
category: "Users"
writes_data: true
---
# Admin Orgs - Grant user access

**Grant user access** — `POST /v1/orgs/{orgId}/users/{userId}/roles/assign`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Orgs - Grant user access"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
POST https://api.atlassian.com/admin/v1/orgs/{{service.org_id}}/users/{{param:userId}}/roles/assign
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `userId` (path, string, required) — The UserId on which the action(Role Assign) needs to happen. Use the Search for users within an organization API to get the userId.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

This API can be used to grant Platform Roles to a user.
