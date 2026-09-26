---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_snippet_changes
title: "Bitbucket - List snippet changes"
kind: request
request: "[[Bitbucket - List snippet changes]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /snippets/{workspace}/{encoded_id}/commits · List snippet changes. Returns the changes (commits) made on this snippet. Writes data: no."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
writes: false
expose: false
---
# bitbucket_list_snippet_changes

`GET /snippets/{workspace}/{encoded_id}/commits` — List snippet changes

- Request: [[Bitbucket - List snippet changes]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
