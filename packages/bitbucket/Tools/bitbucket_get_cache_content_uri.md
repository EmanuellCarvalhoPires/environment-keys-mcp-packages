---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_cache_content_uri
title: "Bitbucket - Get cache content URI"
kind: request
request: "[[Bitbucket - Get cache content URI]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pipelines-config/caches/{cache_uuid}/content-uri · Get cache content URI. Retrieve the URI of the content of the specified cache. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "cache_uuid":
    type: string
    required: true
    description: "The UUID of the cache."
writes: false
expose: false
---
# bitbucket_get_cache_content_uri

`GET /repositories/{workspace}/{repo_slug}/pipelines-config/caches/{cache_uuid}/content-uri` — Get cache content URI

- Request: [[Bitbucket - Get cache content URI]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
