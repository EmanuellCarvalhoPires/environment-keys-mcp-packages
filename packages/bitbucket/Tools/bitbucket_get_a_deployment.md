---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_deployment
title: "Bitbucket - Get a deployment"
kind: request
request: "[[Bitbucket - Get a deployment]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/deployments/{deployment_uuid} · Get a deployment. Retrieve a deployment Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "deployment_uuid":
    type: string
    required: true
    description: "The deployment UUID."
writes: false
expose: false
---
# bitbucket_get_a_deployment

`GET /repositories/{workspace}/{repo_slug}/deployments/{deployment_uuid}` — Get a deployment

- Request: [[Bitbucket - Get a deployment]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
