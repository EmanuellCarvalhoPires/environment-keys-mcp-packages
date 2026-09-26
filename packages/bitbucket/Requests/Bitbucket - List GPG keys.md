---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/gpg
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/users/{selected_user}/gpg-keys"
category: "GPG"
writes_data: false
tool_note: "[[bitbucket_list_gpg_keys]]"
---
# Bitbucket - List GPG keys

**List GPG keys** — `GET /users/{selected_user}/gpg-keys`

- Run by the tool [[bitbucket_list_gpg_keys]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/users/{{param:selected_user}}/gpg-keys
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `selected_user` (path, string, required) — Value of selecteduser in the path.

## Original description

Returns a paginated list of the user's GPG public keys.
The `key` and `subkeys` fields can also be requested from the endpoint.
See [Partial Responses](/cloud/bitbucket/rest/intro/#partial-response) for more details.
