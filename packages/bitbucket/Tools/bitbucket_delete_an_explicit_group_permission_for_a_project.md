---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_an_explicit_group_permission_for_a_project
title: "Bitbucket - Delete an explicit group permission for a project"
kind: request
request: "[[Bitbucket - Delete an explicit group permission for a project]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug} · Delete an explicit group permission for a project. Deletes the project group permission between the requested project and group, if one exists. Only users with admin permission for the project may access this resource. Writes data: yes."
params:
  "project_key":
    type: string
    required: true
    description: "Value of projectkey in the path."
  "group_slug":
    type: string
    required: true
    description: "Value of groupslug in the path."
writes: true
expose: false
---
# bitbucket_delete_an_explicit_group_permission_for_a_project

`DELETE /workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug}` — Delete an explicit group permission for a project

- Request: [[Bitbucket - Delete an explicit group permission for a project]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
