---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_an_explicit_group_permission_for_a_project
title: "Bitbucket - Update an explicit group permission for a project"
kind: request
request: "[[Bitbucket - Update an explicit group permission for a project]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug} · Update an explicit group permission for a project. Updates the group permission, or grants a new permission if one does not already exist. Only users with admin permission for the project may access this resource. Due to security concerns, the JWT and OAuth authentication methods are unsupported. Writes data: yes."
params:
  "project_key":
    type: string
    required: true
    description: "Value of projectkey in the path."
  "group_slug":
    type: string
    required: true
    description: "Value of groupslug in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_update_an_explicit_group_permission_for_a_project

`PUT /workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug}` — Update an explicit group permission for a project

- Request: [[Bitbucket - Update an explicit group permission for a project]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
