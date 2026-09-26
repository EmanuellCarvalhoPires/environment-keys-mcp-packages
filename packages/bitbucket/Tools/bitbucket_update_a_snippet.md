---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_a_snippet
title: "Bitbucket - Update a snippet"
kind: request
request: "[[Bitbucket - Update a snippet]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /snippets/{workspace}/{encoded_id} · Update a snippet. Used to update a snippet. Use this to add and delete files and to change a snippet's title. To update a snippet, one can either PUT a full snapshot, or only the parts that need to be changed. Writes data: yes."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
writes: true
expose: false
---
# bitbucket_update_a_snippet

`PUT /snippets/{workspace}/{encoded_id}` — Update a snippet

- Request: [[Bitbucket - Update a snippet]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
