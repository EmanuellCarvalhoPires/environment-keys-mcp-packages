---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/manage
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin Users]]"
app: "Admin Users"
method: GET
path: "/users/{account_id}/manage"
category: "Manage"
writes_data: false
---
# Admin Users - Get user management permissions

**Get user management permissions** — `GET /users/{account_id}/manage`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Users - Get user management permissions"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-management/rest/

```http
GET https://api.atlassian.com/users/{{param:account_id}}/manage?privileges={{param:privileges}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `account_id` (path, string, required) — The user account to manage
- `privileges` (query, string, optional) — Query parameter privileges.

## Original description

Returns the set of permissions you have for managing the specified Atlassian account
