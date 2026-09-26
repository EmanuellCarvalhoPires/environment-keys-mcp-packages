---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/ssh
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_ssh_key
title: "Bitbucket - Delete a SSH key"
kind: request
request: "[[Bitbucket - Delete a SSH key]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /users/{selected_user}/ssh-keys/{key_id} · Delete a SSH key. Deletes a specific SSH public key from a user's account. Writes data: yes."
params:
  "selected_user":
    type: string
    required: true
    description: "Value of selecteduser in the path."
  "key_id":
    type: string
    required: true
    description: "Value of keyid in the path."
writes: true
expose: false
---
# bitbucket_delete_a_ssh_key

`DELETE /users/{selected_user}/ssh-keys/{key_id}` — Delete a SSH key

- Request: [[Bitbucket - Delete a SSH key]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
