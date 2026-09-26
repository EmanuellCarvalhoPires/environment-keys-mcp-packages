---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_comments_on_a_snippet
title: "Bitbucket - List comments on a snippet"
kind: request
request: "[[Bitbucket - List comments on a snippet]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /snippets/{workspace}/{encoded_id}/comments · List comments on a snippet. Used to retrieve a paginated list of all comments for a specific snippet. This resource works identical to commit and pull request comments. The default sorting is oldest to newest and can be overridden with the sort query parameter. Writes data: no."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
writes: false
expose: false
---
# bitbucket_list_comments_on_a_snippet

`GET /snippets/{workspace}/{encoded_id}/comments` — List comments on a snippet

- Request: [[Bitbucket - List comments on a snippet]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
