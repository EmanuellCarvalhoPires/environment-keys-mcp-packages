---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/ssh
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/users/{selected_user}/ssh-keys/{key_id}"
category: "SSH"
writes_data: true
tool_note: "[[bitbucket_update_a_ssh_key]]"
---
# Bitbucket - Update a SSH key

**Update a SSH key** — `PUT /users/{selected_user}/ssh-keys/{key_id}`

- Run by the tool [[bitbucket_update_a_ssh_key]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/users/{{param:selected_user}}/ssh-keys/{{param:key_id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `selected_user` (path, string, required) — Value of selecteduser in the path.
- `key_id` (path, string, required) — Value of keyid in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates a specific SSH public key on a user's account

Note: Only the 'comment' field can be updated using this API. To modify the key or comment values, you must delete and add the key again.

Example:

```
$ curl -X PUT -H "Content-Type: application/json" -d '{"label": "Work key"}' https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys/{b15b6026-9c02-4626-b4ad-b905f99f763a}
```
