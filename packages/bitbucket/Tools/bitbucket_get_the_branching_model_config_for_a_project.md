---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branching-model
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_the_branching_model_config_for_a_project
title: "Bitbucket - Get the branching model config for a project"
kind: request
request: "[[Bitbucket - Get the branching model config for a project]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/projects/{project_key}/branching-model/settings · Get the branching model config for a project. Return the branching model configuration for a project. The returned object: 1. Always has a development property for the development branch. 2. Always a production property for the production branch. The production branch can be disabled. 3. Writes data: no."
params:
  "project_key":
    type: string
    required: true
    description: "Value of projectkey in the path."
writes: false
expose: false
---
# bitbucket_get_the_branching_model_config_for_a_project

`GET /workspaces/{workspace}/projects/{project_key}/branching-model/settings` — Get the branching model config for a project

- Request: [[Bitbucket - Get the branching model config for a project]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
