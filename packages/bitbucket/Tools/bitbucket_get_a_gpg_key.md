---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/gpg
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_gpg_key
title: "Bitbucket - Get a GPG key"
kind: request
request: "[[Bitbucket - Get a GPG key]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /users/{selected_user}/gpg-keys/{fingerprint} · Get a GPG key. Returns a specific GPG public key belonging to a user. The key and subkeys fields can also be requested from the endpoint. See Partial Responses for more details. Writes data: no."
params:
  "selected_user":
    type: string
    required: true
    description: "Value of selecteduser in the path."
  "fingerprint":
    type: string
    required: true
    description: "Value of fingerprint in the path."
writes: false
expose: false
---
# bitbucket_get_a_gpg_key

`GET /users/{selected_user}/gpg-keys/{fingerprint}` — Get a GPG key

- Request: [[Bitbucket - Get a GPG key]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
