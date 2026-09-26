---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_comment_on_a_snippet
title: "Bitbucket - Create a comment on a snippet"
kind: request
request: "[[Bitbucket - Create a comment on a snippet]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /snippets/{workspace}/{encoded_id}/comments · Create a comment on a snippet. Creates a new comment. The only required field in the body is content.raw. To create a threaded reply to an existing comment, include parent.id. Writes data: yes."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_create_a_comment_on_a_snippet

`POST /snippets/{workspace}/{encoded_id}/comments` — Create a comment on a snippet

- Request: [[Bitbucket - Create a comment on a snippet]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
