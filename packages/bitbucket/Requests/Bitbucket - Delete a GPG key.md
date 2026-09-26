---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/gpg
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/users/{selected_user}/gpg-keys/{fingerprint}"
category: "GPG"
writes_data: true
tool_note: "[[bitbucket_delete_a_gpg_key]]"
---
# Bitbucket - Delete a GPG key

**Delete a GPG key** — `DELETE /users/{selected_user}/gpg-keys/{fingerprint}`

- Run by the tool [[bitbucket_delete_a_gpg_key]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/users/{{param:selected_user}}/gpg-keys/{{param:fingerprint}}
Authorization: {{service.auth_token}}
```

## Parameters

- `selected_user` (path, string, required) — Value of selecteduser in the path.
- `fingerprint` (path, string, required) — Value of fingerprint in the path.

## Original description

Deletes a specific GPG public key from a user's account.
