---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_repository_deploy_key
title: "Bitbucket - Delete a repository deploy key"
kind: request
request: "[[Bitbucket - Delete a repository deploy key]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id} · Delete a repository deploy key. This deletes a deploy key from a repository. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "key_id":
    type: string
    required: true
    description: "Value of keyid in the path."
writes: true
expose: false
---
# bitbucket_delete_a_repository_deploy_key

`DELETE /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}` — Delete a repository deploy key

- Request: [[Bitbucket - Delete a repository deploy key]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
