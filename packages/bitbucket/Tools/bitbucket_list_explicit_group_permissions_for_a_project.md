---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_explicit_group_permissions_for_a_project
title: "Bitbucket - List explicit group permissions for a project"
kind: request
request: "[[Bitbucket - List explicit group permissions for a project]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/projects/{project_key}/permissions-config/groups · List explicit group permissions for a project. Returns a paginated list of explicit group permissions for the given project. This endpoint does not support BBQL features. Writes data: no."
params:
  "project_key":
    type: string
    required: true
    description: "Value of projectkey in the path."
writes: false
expose: false
---
# bitbucket_list_explicit_group_permissions_for_a_project

`GET /workspaces/{workspace}/projects/{project_key}/permissions-config/groups` — List explicit group permissions for a project

- Request: [[Bitbucket - List explicit group permissions for a project]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
