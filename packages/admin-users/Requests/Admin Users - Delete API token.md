---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/api-tokens
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Admin Users]]"
app: "Admin Users"
method: DELETE
path: "/users/{account_id}/manage/api-tokens/{tokenId}"
category: "Api Tokens"
writes_data: true
---
# Admin Users - Delete API token

**Delete API token** — `DELETE /users/{account_id}/manage/api-tokens/{tokenId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin Users - Delete API token"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-management/rest/

```http
DELETE https://api.atlassian.com/users/{{param:account_id}}/manage/api-tokens/{{param:tokenId}}
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `account_id` (path, string, required) — The ID of the user
- `tokenId` (path, string, required) — The ID of the API token

## Original description

Deletes a specifid API token by ID.
