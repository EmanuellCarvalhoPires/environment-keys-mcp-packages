---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/ssh
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/users/{selected_user}/ssh-keys"
category: "SSH"
writes_data: true
tool_note: "[[bitbucket_add_a_new_ssh_key]]"
---
# Bitbucket - Add a new SSH key

**Add a new SSH key** — `POST /users/{selected_user}/ssh-keys`

- Run by the tool [[bitbucket_add_a_new_ssh_key]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/users/{{param:selected_user}}/ssh-keys?expires_on={{param:expires_on}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `selected_user` (path, string, required) — Value of selecteduser in the path.
- `expires_on` (query, string, optional) — The date or date-time of when the key will expire, in ISO-8601 format. Example: YYYY-MM-DDTHH:mm:ss.sssZ
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Adds a new SSH public key to the specified user account and returns the resulting key.

Example:

```
$ curl -X POST -H "Content-Type: application/json" -d '{"key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKqP3Cr632C2dNhhgKVcon4ldUSAeKiku2yP9O9/bDtY user@myhost"}' https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys
```
