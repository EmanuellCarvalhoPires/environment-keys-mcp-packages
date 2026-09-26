---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_check_if_the_current_user_is_watching_a_snippet
title: "Bitbucket - Check if the current user is watching a snippet"
kind: request
request: "[[Bitbucket - Check if the current user is watching a snippet]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /snippets/{workspace}/{encoded_id}/watch · Check if the current user is watching a snippet. Used to check if the current user is watching a specific snippet. Returns 204 (No Content) if the user is watching the snippet and 404 if not. Hitting this endpoint anonymously always returns a 404. Writes data: no."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
writes: false
expose: false
---
# bitbucket_check_if_the_current_user_is_watching_a_snippet

`GET /snippets/{workspace}/{encoded_id}/watch` — Check if the current user is watching a snippet

- Request: [[Bitbucket - Check if the current user is watching a snippet]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
