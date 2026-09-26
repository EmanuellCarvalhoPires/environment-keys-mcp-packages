---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_snippet_for_a_workspace
title: "Bitbucket - Create a snippet for a workspace"
kind: request
request: "[[Bitbucket - Create a snippet for a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /snippets/{workspace} · Create a snippet for a workspace. Identical to /snippets, except that the new snippet will be created under the workspace specified in the path parameter {workspace}. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_create_a_snippet_for_a_workspace

`POST /snippets/{workspace}` — Create a snippet for a workspace

- Request: [[Bitbucket - Create a snippet for a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
