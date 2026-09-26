---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/gpg
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_gpg_keys
title: "Bitbucket - List GPG keys"
kind: request
request: "[[Bitbucket - List GPG keys]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /users/{selected_user}/gpg-keys · List GPG keys. Returns a paginated list of the user's GPG public keys. The key and subkeys fields can also be requested from the endpoint. See Partial Responses for more details. Writes data: no."
params:
  "selected_user":
    type: string
    required: true
    description: "Value of selecteduser in the path."
writes: false
expose: false
---
# bitbucket_list_gpg_keys

`GET /users/{selected_user}/gpg-keys` — List GPG keys

- Request: [[Bitbucket - List GPG keys]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
