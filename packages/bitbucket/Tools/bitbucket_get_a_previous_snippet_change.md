---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_previous_snippet_change
title: "Bitbucket - Get a previous snippet change"
kind: request
request: "[[Bitbucket - Get a previous snippet change]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /snippets/{workspace}/{encoded_id}/commits/{revision} · Get a previous snippet change. Returns the changes made on this snippet in this commit. Writes data: no."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
  "revision":
    type: string
    required: true
    description: "Value of revision in the path."
writes: false
expose: false
---
# bitbucket_get_a_previous_snippet_change

`GET /snippets/{workspace}/{encoded_id}/commits/{revision}` — Get a previous snippet change

- Request: [[Bitbucket - Get a previous snippet change]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
