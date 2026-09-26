---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_a_previous_revision_of_a_snippet
title: "Bitbucket - Update a previous revision of a snippet"
kind: request
request: "[[Bitbucket - Update a previous revision of a snippet]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /snippets/{workspace}/{encoded_id}/{node_id} · Update a previous revision of a snippet. Identical to UPDATE /snippets/encodedid, except that this endpoint takes an explicit commit revision. Only the snippet's \"HEAD\"/\"tip\" (most recent) version can be updated and requests on all other, older revisions fail by returning a 405 status. Writes data: yes."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
  "node_id":
    type: string
    required: true
    description: "Value of nodeid in the path."
writes: true
expose: false
---
# bitbucket_update_a_previous_revision_of_a_snippet

`PUT /snippets/{workspace}/{encoded_id}/{node_id}` — Update a previous revision of a snippet

- Request: [[Bitbucket - Update a previous revision of a snippet]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
