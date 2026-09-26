---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/ssh
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_ssh_keys
title: "Bitbucket - List SSH keys"
kind: request
request: "[[Bitbucket - List SSH keys]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /users/{selected_user}/ssh-keys · List SSH keys. Returns a paginated list of the user's SSH public keys. Writes data: no."
params:
  "selected_user":
    type: string
    required: true
    description: "Value of selecteduser in the path."
writes: false
expose: false
---
# bitbucket_list_ssh_keys

`GET /users/{selected_user}/ssh-keys` — List SSH keys

- Request: [[Bitbucket - List SSH keys]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
