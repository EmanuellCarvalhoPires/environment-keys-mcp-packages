---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/ssh
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/users/{selected_user}/ssh-keys/{key_id}"
category: "SSH"
writes_data: false
tool_note: "[[bitbucket_get_a_ssh_key]]"
---
# Bitbucket - Get a SSH key

**Get a SSH key** — `GET /users/{selected_user}/ssh-keys/{key_id}`

- Run by the tool [[bitbucket_get_a_ssh_key]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/users/{{param:selected_user}}/ssh-keys/{{param:key_id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `selected_user` (path, string, required) — Value of selecteduser in the path.
- `key_id` (path, string, required) — Value of keyid in the path.

## Original description

Returns a specific SSH public key belonging to a user.
