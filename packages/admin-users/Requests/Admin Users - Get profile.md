---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/profile
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin Users]]"
app: "Admin Users"
method: GET
path: "/users/{account_id}/manage/profile"
category: "Profile"
writes_data: false
---
# Admin Users - Get profile

**Get profile** — `GET /users/{account_id}/manage/profile`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Users - Get profile"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-management/rest/

```http
GET https://api.atlassian.com/users/{{param:account_id}}/manage/profile
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `account_id` (path, string, required) — The ID of the user

## Original description

Returns information about a single Atlassian account by ID
