---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-roles
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_project_role
title: "Jira v3 - Delete project role"
kind: request
request: "[[Jira v3 - Delete project role]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/role/{id} · Delete project role. Deletes a project role. You must specify a replacement project role if you wish to delete a project role that is in use. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the project role to delete. Use Get all project roles to get a list of project role IDs."
  "swap":
    type: string
    required: false
    description: "The ID of the project role that will replace the one being deleted. The swap will attempt to swap the role in schemes (notifications, permissions, issue security), workflows, worklogs and comments."
writes: true
expose: false
---
# jira_delete_project_role

`DELETE /rest/api/3/role/{id}` — Delete project role

- Request: [[Jira v3 - Delete project role]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
