---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_a_known_host
title: "Bitbucket - Update a known host"
kind: request
request: "[[Bitbucket - Update a known host]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid} · Update a known host. Update a repository level known host. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "known_host_uuid":
    type: string
    required: true
    description: "The UUID of the known host to update."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_update_a_known_host

`PUT /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}` — Update a known host

- Request: [[Bitbucket - Update a known host]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
