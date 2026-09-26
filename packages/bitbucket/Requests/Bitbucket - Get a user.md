---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/users
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/users/{selected_user}"
category: "Users"
writes_data: false
tool_note: "[[bitbucket_get_a_user]]"
---
# Bitbucket - Get a user

**Get a user** — `GET /users/{selected_user}`

- Run by the tool [[bitbucket_get_a_user]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/users/{{param:selected_user}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `selected_user` (path, string, required) — Value of selecteduser in the path.

## Original description

Gets the public information associated with a user account.

If the user's profile is private, `location`, `website` and
`created_on` elements are omitted.

Note that the user object returned by this operation is changing significantly, due to privacy changes.
See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-gdpr/#changes-to-bitbucket-user-objects) for details.
