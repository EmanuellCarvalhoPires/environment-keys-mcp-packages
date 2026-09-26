---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/ssh
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_add_a_new_ssh_key
title: "Bitbucket - Add a new SSH key"
kind: request
request: "[[Bitbucket - Add a new SSH key]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /users/{selected_user}/ssh-keys · Add a new SSH key. Adds a new SSH public key to the specified user account and returns the resulting key. Writes data: yes."
params:
  "selected_user":
    type: string
    required: true
    description: "Value of selecteduser in the path."
  "expires_on":
    type: string
    required: false
    description: "The date or date-time of when the key will expire, in ISO-8601 format. Example: YYYY-MM-DDTHH:mm:ss.sssZ"
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_add_a_new_ssh_key

`POST /users/{selected_user}/ssh-keys` — Add a new SSH key

- Request: [[Bitbucket - Add a new SSH key]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
