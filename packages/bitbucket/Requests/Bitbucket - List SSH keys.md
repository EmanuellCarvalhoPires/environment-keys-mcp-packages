---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/ssh
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/users/{selected_user}/ssh-keys"
category: "SSH"
writes_data: false
tool_note: "[[bitbucket_list_ssh_keys]]"
---
# Bitbucket - List SSH keys

**List SSH keys** — `GET /users/{selected_user}/ssh-keys`

- Run by the tool [[bitbucket_list_ssh_keys]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/users/{{param:selected_user}}/ssh-keys
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `selected_user` (path, string, required) — Value of selecteduser in the path.

## Original description

Returns a paginated list of the user's SSH public keys.
