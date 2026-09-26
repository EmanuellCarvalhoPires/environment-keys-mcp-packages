---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_snippets_in_a_workspace
title: "Bitbucket - List snippets in a workspace"
kind: request
request: "[[Bitbucket - List snippets in a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /snippets/{workspace} · List snippets in a workspace. Returns a paginated list of snippets owned by {workspace}. To limit the set of returned snippets, apply the ?role=[owner|contributor|member] query parameter where the roles are defined as follows: owner: snippets owned by {workspace} that also belong to the current user (only ret… Writes data: no."
params:
  "role":
    type: string
    required: false
    description: "Filter down the result based on the authenticated user's role (owner, contributor, or member)."
writes: false
expose: false
---
# bitbucket_list_snippets_in_a_workspace

`GET /snippets/{workspace}` — List snippets in a workspace

- Request: [[Bitbucket - List snippets in a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
