---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_ssh_key_pair
title: "Bitbucket - Get SSH key pair"
kind: request
request: "[[Bitbucket - Get SSH key pair]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair · Get SSH key pair. Retrieve the repository SSH key pair excluding the SSH private key. The private key is a write only field and will never be exposed in the logs or the REST API. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
writes: false
expose: false
---
# bitbucket_get_ssh_key_pair

`GET /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair` — Get SSH key pair

- Request: [[Bitbucket - Get SSH key pair]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
