---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/profile
  - api/operation/update
  - api/effect/write
up: "[[MCP - Admin Users]]"
app: "Admin Users"
method: PATCH
path: "/users/{account_id}/manage/profile"
category: "Profile"
writes_data: true
---
# Admin Users - Update profile

**Update profile** — `PATCH /users/{account_id}/manage/profile`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Users - Update profile"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-management/rest/

```http
PATCH https://api.atlassian.com/users/{{param:account_id}}/manage/profile
Authorization: {{service.admin_auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `account_id` (path, string, required) — The ID of the user to update
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates fields in a user account. The `profile.write` privilege details which fields you can change.
