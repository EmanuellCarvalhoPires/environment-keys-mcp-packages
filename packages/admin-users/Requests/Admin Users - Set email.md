---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/email
  - api/operation/update
  - api/effect/write
up: "[[MCP - Admin Users]]"
app: "Admin Users"
method: PUT
path: "/users/{account_id}/manage/email"
category: "Email"
writes_data: true
---
# Admin Users - Set email

**Set email** — `PUT /users/{account_id}/manage/email`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Users - Set email"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-management/rest/

```http
PUT https://api.atlassian.com/users/{{param:account_id}}/manage/email
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `account_id` (path, string, required) — The ID of the user
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Sets the specified user's email address. Before using this endpoint, you must [verify the target domain](https://confluence.atlassian.com/x/gjcWN) as the new email address will be considered verified.
The permission to make use of this resource is exposed by the `email.set` privilege.
This call invalidates all active sessions.
