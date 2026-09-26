---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_a_comment_on_a_snippet
title: "Bitbucket - Update a comment on a snippet"
kind: request
request: "[[Bitbucket - Update a comment on a snippet]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /snippets/{workspace}/{encoded_id}/comments/{comment_id} · Update a comment on a snippet. Updates a comment. The only required field in the body is content.raw. Comments can only be updated by their author. Writes data: yes."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
  "comment_id":
    type: string
    required: true
    description: "Value of commentid in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_update_a_comment_on_a_snippet

`PUT /snippets/{workspace}/{encoded_id}/comments/{comment_id}` — Update a comment on a snippet

- Request: [[Bitbucket - Update a comment on a snippet]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
