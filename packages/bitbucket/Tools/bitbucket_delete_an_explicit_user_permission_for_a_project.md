---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_an_explicit_user_permission_for_a_project
title: "Bitbucket - Delete an explicit user permission for a project"
kind: request
request: "[[Bitbucket - Delete an explicit user permission for a project]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /workspaces/{workspace}/projects/{project_key}/permissions-config/users/{selected_user_id} · Delete an explicit user permission for a project. Deletes the project user permission between the requested project and user, if one exists. Only users with admin permission for the project may access this resource. Due to security concerns, the JWT and OAuth authentication methods are unsupported. Writes data: yes."
params:
  "project_key":
    type: string
    required: true
    description: "Value of projectkey in the path."
  "selected_user_id":
    type: string
    required: true
    description: "Value of selecteduserid in the path."
writes: true
expose: false
---
# bitbucket_delete_an_explicit_user_permission_for_a_project

`DELETE /workspaces/{workspace}/projects/{project_key}/permissions-config/users/{selected_user_id}` — Delete an explicit user permission for a project

- Request: [[Bitbucket - Delete an explicit user permission for a project]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
