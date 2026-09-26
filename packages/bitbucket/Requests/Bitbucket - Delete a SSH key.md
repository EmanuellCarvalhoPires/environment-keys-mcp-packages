---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/ssh
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/users/{selected_user}/ssh-keys/{key_id}"
category: "SSH"
writes_data: true
tool_note: "[[bitbucket_delete_a_ssh_key]]"
---
# Bitbucket - Delete a SSH key

**Delete a SSH key** — `DELETE /users/{selected_user}/ssh-keys/{key_id}`

- Run by the tool [[bitbucket_delete_a_ssh_key]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/users/{{param:selected_user}}/ssh-keys/{{param:key_id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `selected_user` (path, string, required) — Value of selecteduser in the path.
- `key_id` (path, string, required) — Value of keyid in the path.

## Original description

Deletes a specific SSH public key from a user's account.
