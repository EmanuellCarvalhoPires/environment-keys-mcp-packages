---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_watch_a_snippet
title: "Bitbucket - Watch a snippet"
kind: request
request: "[[Bitbucket - Watch a snippet]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /snippets/{workspace}/{encoded_id}/watch · Watch a snippet. Used to start watching a specific snippet. Returns 204 (No Content). Writes data: yes."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
writes: true
expose: false
---
# bitbucket_watch_a_snippet

`PUT /snippets/{workspace}/{encoded_id}/watch` — Watch a snippet

- Request: [[Bitbucket - Watch a snippet]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
