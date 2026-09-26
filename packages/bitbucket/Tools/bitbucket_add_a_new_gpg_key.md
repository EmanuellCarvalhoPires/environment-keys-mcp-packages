---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/gpg
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_add_a_new_gpg_key
title: "Bitbucket - Add a new GPG key"
kind: request
request: "[[Bitbucket - Add a new GPG key]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /users/{selected_user}/gpg-keys · Add a new GPG key. Adds a new GPG public key to the specified user account and returns the resulting key. Example: $ curl -X POST -H \"Content-Type: application/json\" -d '{\"key\": \"\"}' https://api.bitbucket.org/2.0/users/{d7dd0e2d-3994-4a50-a9ee-d260b6cefdab}/gpg-keys Writes data: yes."
params:
  "selected_user":
    type: string
    required: true
    description: "Value of selecteduser in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_add_a_new_gpg_key

`POST /users/{selected_user}/gpg-keys` — Add a new GPG key

- Request: [[Bitbucket - Add a new GPG key]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
