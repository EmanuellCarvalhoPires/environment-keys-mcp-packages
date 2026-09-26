---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_ssh_key_pair
title: "Bitbucket - Update SSH key pair"
kind: request
request: "[[Bitbucket - Update SSH key pair]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair · Update SSH key pair. Create or update the repository SSH key pair. The private key will be set as a default SSH identity in your build container. Writes data: yes."
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
# bitbucket_update_ssh_key_pair

`PUT /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair` — Update SSH key pair

- Request: [[Bitbucket - Update SSH key pair]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
