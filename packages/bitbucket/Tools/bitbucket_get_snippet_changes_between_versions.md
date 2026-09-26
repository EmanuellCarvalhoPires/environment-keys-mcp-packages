---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_snippet_changes_between_versions
title: "Bitbucket - Get snippet changes between versions"
kind: request
request: "[[Bitbucket - Get snippet changes between versions]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /snippets/{workspace}/{encoded_id}/{revision}/diff · Get snippet changes between versions. Returns the diff of the specified commit against its first parent. Note that this resource is different in functionality from the patch resource. Writes data: no."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
  "revision":
    type: string
    required: true
    description: "Value of revision in the path."
  "path":
    type: string
    required: false
    description: "When used, only one the diff of the specified file will be returned."
writes: false
expose: false
---
# bitbucket_get_snippet_changes_between_versions

`GET /snippets/{workspace}/{encoded_id}/{revision}/diff` — Get snippet changes between versions

- Request: [[Bitbucket - Get snippet changes between versions]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
