---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/gpg
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/users/{selected_user}/gpg-keys"
category: "GPG"
writes_data: true
tool_note: "[[bitbucket_add_a_new_gpg_key]]"
---
# Bitbucket - Add a new GPG key

**Add a new GPG key** — `POST /users/{selected_user}/gpg-keys`

- Run by the tool [[bitbucket_add_a_new_gpg_key]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/users/{{param:selected_user}}/gpg-keys
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `selected_user` (path, string, required) — Value of selecteduser in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Adds a new GPG public key to the specified user account and returns the resulting key.

Example:

```
$ curl -X POST -H "Content-Type: application/json" -d
'{"key": ""}'
https://api.bitbucket.org/2.0/users/{d7dd0e2d-3994-4a50-a9ee-d260b6cefdab}/gpg-keys
```
