---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_users_watching_a_snippet
title: "Bitbucket - List users watching a snippet"
kind: request
request: "[[Bitbucket - List users watching a snippet]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /snippets/{workspace}/{encoded_id}/watchers · List users watching a snippet. Returns a paginated list of all users watching a specific snippet. Writes data: no."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
writes: false
expose: false
---
# bitbucket_list_users_watching_a_snippet

`GET /snippets/{workspace}/{encoded_id}/watchers` — List users watching a snippet

- Request: [[Bitbucket - List users watching a snippet]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
