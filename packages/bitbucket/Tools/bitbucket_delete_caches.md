---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_caches
title: "Bitbucket - Delete caches"
kind: request
request: "[[Bitbucket - Delete caches]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/pipelines-config/caches · Delete caches. Delete repository cache versions by name. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "name":
    type: string
    required: true
    description: "The cache name."
writes: true
expose: false
---
# bitbucket_delete_caches

`DELETE /repositories/{workspace}/{repo_slug}/pipelines-config/caches` — Delete caches

- Request: [[Bitbucket - Delete caches]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
