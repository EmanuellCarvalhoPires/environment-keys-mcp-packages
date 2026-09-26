---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_ssh_key_pair
title: "Bitbucket - Delete SSH key pair"
kind: request
request: "[[Bitbucket - Delete SSH key pair]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair · Delete SSH key pair. Delete the repository SSH key pair. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
writes: true
expose: false
---
# bitbucket_delete_ssh_key_pair

`DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair` — Delete SSH key pair

- Request: [[Bitbucket - Delete SSH key pair]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
