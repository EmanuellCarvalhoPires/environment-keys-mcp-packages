---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/gpg
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_gpg_key
title: "Bitbucket - Delete a GPG key"
kind: request
request: "[[Bitbucket - Delete a GPG key]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /users/{selected_user}/gpg-keys/{fingerprint} · Delete a GPG key. Deletes a specific GPG public key from a user's account. Writes data: yes."
params:
  "selected_user":
    type: string
    required: true
    description: "Value of selecteduser in the path."
  "fingerprint":
    type: string
    required: true
    description: "Value of fingerprint in the path."
writes: true
expose: false
---
# bitbucket_delete_a_gpg_key

`DELETE /users/{selected_user}/gpg-keys/{fingerprint}` — Delete a GPG key

- Request: [[Bitbucket - Delete a GPG key]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
