---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_known_host
title: "Bitbucket - Create a known host"
kind: request
request: "[[Bitbucket - Create a known host]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts · Create a known host. Create a repository level known host. Writes data: yes."
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
# bitbucket_create_a_known_host

`POST /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts` — Create a known host

- Request: [[Bitbucket - Create a known host]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
