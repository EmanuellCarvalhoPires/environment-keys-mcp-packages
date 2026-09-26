---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_stop_watching_a_snippet
title: "Bitbucket - Stop watching a snippet"
kind: request
request: "[[Bitbucket - Stop watching a snippet]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /snippets/{workspace}/{encoded_id}/watch · Stop watching a snippet. Used to stop watching a specific snippet. Returns 204 (No Content) to indicate success. Writes data: yes."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
writes: true
expose: false
---
# bitbucket_stop_watching_a_snippet

`DELETE /snippets/{workspace}/{encoded_id}/watch` — Stop watching a snippet

- Request: [[Bitbucket - Stop watching a snippet]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
