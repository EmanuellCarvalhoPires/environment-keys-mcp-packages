---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/ssh
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_ssh_key
title: "Bitbucket - Get a SSH key"
kind: request
request: "[[Bitbucket - Get a SSH key]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /users/{selected_user}/ssh-keys/{key_id} · Get a SSH key. Returns a specific SSH public key belonging to a user. Writes data: no."
params:
  "selected_user":
    type: string
    required: true
    description: "Value of selecteduser in the path."
  "key_id":
    type: string
    required: true
    description: "Value of keyid in the path."
writes: false
expose: false
---
# bitbucket_get_a_ssh_key

`GET /users/{selected_user}/ssh-keys/{key_id}` — Get a SSH key

- Request: [[Bitbucket - Get a SSH key]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
