---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_known_host
title: "Bitbucket - Delete a known host"
kind: request
request: "[[Bitbucket - Delete a known host]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid} · Delete a known host. Delete a repository level known host. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "known_host_uuid":
    type: string
    required: true
    description: "The UUID of the known host to delete."
writes: true
expose: false
---
# bitbucket_delete_a_known_host

`DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}` — Delete a known host

- Request: [[Bitbucket - Delete a known host]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
