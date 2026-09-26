---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_project_for_a_workspace
title: "Bitbucket - Delete a project for a workspace"
kind: request
request: "[[Bitbucket - Delete a project for a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /workspaces/{workspace}/projects/{project_key} · Delete a project for a workspace. Deletes this project. This is an irreversible operation. You cannot delete a project that still contains repositories. To delete the project, delete or transfer the repositories first. Example: $ curl -X DELETE https://api.bitbucket.org/2.0/workspaces/bbworkspace1/projects/PROJ Writes data: yes."
params:
  "project_key":
    type: string
    required: true
    description: "Value of projectkey in the path."
writes: true
expose: false
---
# bitbucket_delete_a_project_for_a_workspace

`DELETE /workspaces/{workspace}/projects/{project_key}` — Delete a project for a workspace

- Request: [[Bitbucket - Delete a project for a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
