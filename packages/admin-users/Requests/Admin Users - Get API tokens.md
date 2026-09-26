---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/api-tokens
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin Users]]"
app: "Admin Users"
method: GET
path: "/users/{account_id}/manage/api-tokens"
category: "Api Tokens"
writes_data: false
---
# Admin Users - Get API tokens

**Get API tokens** — `GET /users/{account_id}/manage/api-tokens`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Users - Get API tokens"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-management/rest/

```http
GET https://api.atlassian.com/users/{{param:account_id}}/manage/api-tokens
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `account_id` (path, string, required) — The ID of the user

## Original description

Gets the API tokens owned by the specified user.
