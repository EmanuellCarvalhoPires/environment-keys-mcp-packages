---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_project_deploy_key
title: "Bitbucket - Get a project deploy key"
kind: request
request: "[[Bitbucket - Get a project deploy key]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/projects/{project_key}/deploy-keys/{key_id} · Get a project deploy key. Returns the deploy key belonging to a specific key ID. Writes data: no."
params:
  "project_key":
    type: string
    required: true
    description: "Value of projectkey in the path."
  "key_id":
    type: string
    required: true
    description: "Value of keyid in the path."
writes: false
expose: false
---
# bitbucket_get_a_project_deploy_key

`GET /workspaces/{workspace}/projects/{project_key}/deploy-keys/{key_id}` — Get a project deploy key

- Request: [[Bitbucket - Get a project deploy key]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
