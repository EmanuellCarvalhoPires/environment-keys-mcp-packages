---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/gpg
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/users/{selected_user}/gpg-keys/{fingerprint}"
category: "GPG"
writes_data: false
tool_note: "[[bitbucket_get_a_gpg_key]]"
---
# Bitbucket - Get a GPG key

**Get a GPG key** — `GET /users/{selected_user}/gpg-keys/{fingerprint}`

- Run by the tool [[bitbucket_get_a_gpg_key]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/users/{{param:selected_user}}/gpg-keys/{{param:fingerprint}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `selected_user` (path, string, required) — Value of selecteduser in the path.
- `fingerprint` (path, string, required) — Value of fingerprint in the path.

## Original description

Returns a specific GPG public key belonging to a user.
The `key` and `subkeys` fields can also be requested from the endpoint.
See [Partial Responses](/cloud/bitbucket/rest/intro/#partial-response) for more details.
