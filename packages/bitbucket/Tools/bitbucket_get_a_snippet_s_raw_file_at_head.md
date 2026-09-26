---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_snippet_s_raw_file_at_head
title: "Bitbucket - Get a snippet's raw file at HEAD"
kind: request
request: "[[Bitbucket - Get a snippet's raw file at HEAD]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /snippets/{workspace}/{encoded_id}/files/{path} · Get a snippet's raw file at HEAD. Convenience resource for getting to a snippet's raw files without the need for first having to retrieve the snippet itself and having to pull out the versioned file links. Writes data: no."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
  "path":
    type: string
    required: true
    description: "Value of path in the path."
writes: false
expose: false
---
# bitbucket_get_a_snippet_s_raw_file_at_head

`GET /snippets/{workspace}/{encoded_id}/files/{path}` — Get a snippet's raw file at HEAD

- Request: [[Bitbucket - Get a snippet's raw file at HEAD]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
