---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_the_next_build_number
title: "Bitbucket - Update the next build number"
kind: request
request: "[[Bitbucket - Update the next build number]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/pipelines_config/build_number · Update the next build number. Update the next build number that should be assigned to a pipeline. The next build number that will be configured has to be strictly higher than the current latest build number for this repository. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_update_the_next_build_number

`PUT /repositories/{workspace}/{repo_slug}/pipelines_config/build_number` — Update the next build number

- Request: [[Bitbucket - Update the next build number]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
