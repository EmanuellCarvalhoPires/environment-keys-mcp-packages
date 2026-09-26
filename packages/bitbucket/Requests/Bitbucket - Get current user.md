---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/users
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/user"
category: "Users"
writes_data: false
tool_note: "[[bitbucket_get_current_user]]"
---
# Bitbucket - Get current user

**Get current user** — `GET /user`

- Run by the tool [[bitbucket_get_current_user]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/user
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns the currently logged in user.
