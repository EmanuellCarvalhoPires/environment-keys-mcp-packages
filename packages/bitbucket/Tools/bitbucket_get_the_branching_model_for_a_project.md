---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branching-model
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_the_branching_model_for_a_project
title: "Bitbucket - Get the branching model for a project"
kind: request
request: "[[Bitbucket - Get the branching model for a project]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/projects/{project_key}/branching-model · Get the branching model for a project. Return the branching model set at the project level. This view is read-only. The branching model settings can be changed using the settings API. The returned object: 1. Always has a development property. Writes data: no."
params:
  "project_key":
    type: string
    required: true
    description: "Value of projectkey in the path."
writes: false
expose: false
---
# bitbucket_get_the_branching_model_for_a_project

`GET /workspaces/{workspace}/projects/{project_key}/branching-model` — Get the branching model for a project

- Request: [[Bitbucket - Get the branching model for a project]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
