---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/ssh
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_a_ssh_key
title: "Bitbucket - Update a SSH key"
kind: request
request: "[[Bitbucket - Update a SSH key]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /users/{selected_user}/ssh-keys/{key_id} · Update a SSH key. Updates a specific SSH public key on a user's account Note: Only the 'comment' field can be updated using this API. To modify the key or comment values, you must delete and add the key again. Writes data: yes."
params:
  "selected_user":
    type: string
    required: true
    description: "Value of selecteduser in the path."
  "key_id":
    type: string
    required: true
    description: "Value of keyid in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_update_a_ssh_key

`PUT /users/{selected_user}/ssh-keys/{key_id}` — Update a SSH key

- Request: [[Bitbucket - Update a SSH key]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
