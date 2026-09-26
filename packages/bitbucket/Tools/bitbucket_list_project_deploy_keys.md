---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_project_deploy_keys
title: "Bitbucket - List project deploy keys"
kind: request
request: "[[Bitbucket - List project deploy keys]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/projects/{project_key}/deploy-keys · List project deploy keys. Returns all deploy keys belonging to a project. Writes data: no."
params:
  "project_key":
    type: string
    required: true
    description: "Value of projectkey in the path."
writes: false
expose: false
---
# bitbucket_list_project_deploy_keys

`GET /workspaces/{workspace}/projects/{project_key}/deploy-keys` — List project deploy keys

- Request: [[Bitbucket - List project deploy keys]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
