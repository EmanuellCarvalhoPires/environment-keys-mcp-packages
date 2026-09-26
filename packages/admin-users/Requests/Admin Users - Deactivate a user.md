---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/lifecycle
  - api/operation/action
  - api/effect/write
up: "[[MCP - Admin Users]]"
app: "Admin Users"
method: POST
path: "/users/{account_id}/manage/lifecycle/disable"
category: "Lifecycle"
writes_data: true
---
# Admin Users - Deactivate a user

**Deactivate a user** — `POST /users/{account_id}/manage/lifecycle/disable`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Users - Deactivate a user"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-management/rest/

```http
POST https://api.atlassian.com/users/{{param:account_id}}/manage/lifecycle/disable
Authorization: {{service.admin_auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `account_id` (path, string, required) — The ID of the user
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Deactivate (block) the specified user account from logging into Atlassian. The permission to make use of this resource is exposed by the `lifecycle.enablement` privilege.
You can optionally set a message associated with the block. If none is supplied, a default message will be used.
