---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_a_repository_deploy_key
title: "Bitbucket - Update a repository deploy key"
kind: request
request: "[[Bitbucket - Update a repository deploy key]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id} · Update a repository deploy key. Update an existing deploy key in a repository. The same key needs to be passed in but the comment and label can change. Writes data: yes."
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
# bitbucket_update_a_repository_deploy_key

`PUT /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}` — Update a repository deploy key

- Request: [[Bitbucket - Update a repository deploy key]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
