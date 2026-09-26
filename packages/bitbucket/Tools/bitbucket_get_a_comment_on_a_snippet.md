---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_comment_on_a_snippet
title: "Bitbucket - Get a comment on a snippet"
kind: request
request: "[[Bitbucket - Get a comment on a snippet]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /snippets/{workspace}/{encoded_id}/comments/{comment_id} · Get a comment on a snippet. Returns the specific snippet comment. Writes data: no."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
  "comment_id":
    type: string
    required: true
    description: "Value of commentid in the path."
writes: false
expose: false
---
# bitbucket_get_a_comment_on_a_snippet

`GET /snippets/{workspace}/{encoded_id}/comments/{comment_id}` — Get a comment on a snippet

- Request: [[Bitbucket - Get a comment on a snippet]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
