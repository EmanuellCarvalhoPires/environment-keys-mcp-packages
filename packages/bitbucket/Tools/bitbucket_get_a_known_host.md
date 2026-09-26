---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_known_host
title: "Bitbucket - Get a known host"
kind: request
request: "[[Bitbucket - Get a known host]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid} · Get a known host. Retrieve a repository level known host. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "known_host_uuid":
    type: string
    required: true
    description: "The UUID of the known host to retrieve."
writes: false
expose: false
---
# bitbucket_get_a_known_host

`GET /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}` — Get a known host

- Request: [[Bitbucket - Get a known host]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
