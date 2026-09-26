---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_an_explicit_group_permission_for_a_project
title: "Bitbucket - Get an explicit group permission for a project"
kind: request
request: "[[Bitbucket - Get an explicit group permission for a project]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug} · Get an explicit group permission for a project. Returns the group permission for a given group and project. Only users with admin permission for the project may access this resource. Permissions can be: admin create-repo write read none Writes data: no."
params:
  "project_key":
    type: string
    required: true
    description: "Value of projectkey in the path."
  "group_slug":
    type: string
    required: true
    description: "Value of groupslug in the path."
writes: false
expose: false
---
# bitbucket_get_an_explicit_group_permission_for_a_project

`GET /workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug}` — Get an explicit group permission for a project

- Request: [[Bitbucket - Get an explicit group permission for a project]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
