---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-roles
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_partial_update_project_role
title: "Jira v3 - Partial update project role"
kind: request
request: "[[Jira v3 - Partial update project role]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/role/{id} · Partial update project role. Updates either the project role's name or its description. You cannot update both the name and description at the same time using this operation. If you send a request with a name and a description only the name is updated. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the project role. Use Get all project roles to get a list of project role IDs."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_partial_update_project_role

`POST /rest/api/3/role/{id}` — Partial update project role

- Request: [[Jira v3 - Partial update project role]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
