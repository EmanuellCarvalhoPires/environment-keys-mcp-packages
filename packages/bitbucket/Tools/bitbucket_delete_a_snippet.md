---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_snippet
title: "Bitbucket - Delete a snippet"
kind: request
request: "[[Bitbucket - Delete a snippet]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /snippets/{workspace}/{encoded_id} · Delete a snippet. Deletes a snippet and returns an empty response. Writes data: yes."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
writes: true
expose: false
---
# bitbucket_delete_a_snippet

`DELETE /snippets/{workspace}/{encoded_id}` — Delete a snippet

- Request: [[Bitbucket - Delete a snippet]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
