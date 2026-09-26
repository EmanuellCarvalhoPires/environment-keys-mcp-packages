---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_project_for_a_workspace
title: "Bitbucket - Get a project for a workspace"
kind: request
request: "[[Bitbucket - Get a project for a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/projects/{project_key} · Get a project for a workspace. Returns the requested project. Writes data: no."
params:
  "project_key":
    type: string
    required: true
    description: "Value of projectkey in the path."
writes: false
expose: false
---
# bitbucket_get_a_project_for_a_workspace

`GET /workspaces/{workspace}/projects/{project_key}` — Get a project for a workspace

- Request: [[Bitbucket - Get a project for a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
