---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_previous_revision_of_a_snippet
title: "Bitbucket - Delete a previous revision of a snippet"
kind: request
request: "[[Bitbucket - Delete a previous revision of a snippet]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /snippets/{workspace}/{encoded_id}/{node_id} · Delete a previous revision of a snippet. Deletes the snippet. Note that this only works for versioned URLs that point to the latest commit of the snippet. Pointing to an older commit results in a 405 status code. Writes data: yes."
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
# bitbucket_delete_a_previous_revision_of_a_snippet

`DELETE /snippets/{workspace}/{encoded_id}/{node_id}` — Delete a previous revision of a snippet

- Request: [[Bitbucket - Delete a previous revision of a snippet]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
