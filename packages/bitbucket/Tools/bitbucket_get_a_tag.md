---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/refs
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_tag
title: "Bitbucket - Get a tag"
kind: request
request: "[[Bitbucket - Get a tag]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/refs/tags/{name} · Get a tag. Returns the specified tag. $ curl -s https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8 -G | jq . Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "name":
    type: string
    required: true
    description: "Value of name in the path."
writes: false
expose: false
---
# bitbucket_get_a_tag

`GET /repositories/{workspace}/{repo_slug}/refs/tags/{name}` — Get a tag

- Request: [[Bitbucket - Get a tag]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
