---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_snippet
title: "Bitbucket - Create a snippet"
kind: request
request: "[[Bitbucket - Create a snippet]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /snippets · Create a snippet. Creates a new snippet under the authenticated user's account. Snippets can contain multiple files. Both text and binary files are supported. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_create_a_snippet

`POST /snippets` — Create a snippet

- Request: [[Bitbucket - Create a snippet]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
