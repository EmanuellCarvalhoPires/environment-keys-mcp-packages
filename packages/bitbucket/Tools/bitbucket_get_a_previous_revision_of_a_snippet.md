---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_previous_revision_of_a_snippet
title: "Bitbucket - Get a previous revision of a snippet"
kind: request
request: "[[Bitbucket - Get a previous revision of a snippet]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /snippets/{workspace}/{encoded_id}/{node_id} · Get a previous revision of a snippet. Identical to GET /snippets/encodedid, except that this endpoint can be used to retrieve the contents of the snippet as it was at an older revision, while /snippets/encodedid always returns the snippet's current revision. Writes data: no."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
  "node_id":
    type: string
    required: true
    description: "Value of nodeid in the path."
writes: false
expose: false
---
# bitbucket_get_a_previous_revision_of_a_snippet

`GET /snippets/{workspace}/{encoded_id}/{node_id}` — Get a previous revision of a snippet

- Request: [[Bitbucket - Get a previous revision of a snippet]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
