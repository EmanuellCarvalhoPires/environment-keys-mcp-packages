---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branching-model
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_the_branching_model_config_for_a_project
title: "Bitbucket - Update the branching model config for a project"
kind: request
request: "[[Bitbucket - Update the branching model config for a project]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /workspaces/{workspace}/projects/{project_key}/branching-model/settings · Update the branching model config for a project. Update the branching model configuration for a project. The development branch can be configured to a specific branch or to track the main branch. Writes data: yes."
params:
  "project_key":
    type: string
    required: true
    description: "Value of projectkey in the path."
writes: true
expose: false
---
# bitbucket_update_the_branching_model_config_for_a_project

`PUT /workspaces/{workspace}/projects/{project_key}/branching-model/settings` — Update the branching model config for a project

- Request: [[Bitbucket - Update the branching model config for a project]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
