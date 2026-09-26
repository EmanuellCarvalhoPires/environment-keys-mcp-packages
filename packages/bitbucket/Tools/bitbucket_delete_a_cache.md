---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_cache
title: "Bitbucket - Delete a cache"
kind: request
request: "[[Bitbucket - Delete a cache]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/pipelines-config/caches/{cache_uuid} · Delete a cache. Delete a repository cache. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "cache_uuid":
    type: string
    required: true
    description: "The UUID of the cache to delete."
writes: true
expose: false
---
# bitbucket_delete_a_cache

`DELETE /repositories/{workspace}/{repo_slug}/pipelines-config/caches/{cache_uuid}` — Delete a cache

- Request: [[Bitbucket - Delete a cache]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
