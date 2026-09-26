---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_snippet
title: "Bitbucket - Get a snippet"
kind: request
request: "[[Bitbucket - Get a snippet]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /snippets/{workspace}/{encoded_id} · Get a snippet. Retrieves a single snippet. Snippets support multiple content types: application/json multipart/related multipart/form-data application/json ---------------- The default content type of the response is application/json. Writes data: no."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
writes: false
expose: false
---
# bitbucket_get_a_snippet

`GET /snippets/{workspace}/{encoded_id}` — Get a snippet

- Request: [[Bitbucket - Get a snippet]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
