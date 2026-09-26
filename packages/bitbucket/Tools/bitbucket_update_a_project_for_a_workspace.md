---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_a_project_for_a_workspace
title: "Bitbucket - Update a project for a workspace"
kind: request
request: "[[Bitbucket - Update a project for a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /workspaces/{workspace}/projects/{project_key} · Update a project for a workspace. Since this endpoint can be used to both update and to create a project, the request body depends on the intent. Creation See the POST documentation for the project collection for an example of the request body. Writes data: yes."
params:
  "project_key":
    type: string
    required: true
    description: "Value of projectkey in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_update_a_project_for_a_workspace

`PUT /workspaces/{workspace}/projects/{project_key}` — Update a project for a workspace

- Request: [[Bitbucket - Update a project for a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
