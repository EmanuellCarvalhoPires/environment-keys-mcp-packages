---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_snippet_s_raw_file
title: "Bitbucket - Get a snippet's raw file"
kind: request
request: "[[Bitbucket - Get a snippet's raw file]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /snippets/{workspace}/{encoded_id}/{node_id}/files/{path} · Get a snippet's raw file. Retrieves the raw contents of a specific file in the snippet. The Content-Disposition header will be \"attachment\" to avoid issues with malevolent executable files. The file's mime type is derived from its filename and returned in the Content-Type header. Writes data: no."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
  "node_id":
    type: string
    required: true
    description: "Value of nodeid in the path."
  "path":
    type: string
    required: true
    description: "Value of path in the path."
writes: false
expose: false
---
# bitbucket_get_a_snippet_s_raw_file

`GET /snippets/{workspace}/{encoded_id}/{node_id}/files/{path}` — Get a snippet's raw file

- Request: [[Bitbucket - Get a snippet's raw file]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
