---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-roles
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_fully_update_project_role
title: "Jira v3 - Fully update project role"
kind: request
request: "[[Jira v3 - Fully update project role]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/role/{id} · Fully update project role. Updates the project role's name and description. You must include both a name and a description in the request. Permissions required: Administer Jira global permission. Writes data: yes."
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
# jira_fully_update_project_role

`PUT /rest/api/3/role/{id}` — Fully update project role

- Request: [[Jira v3 - Fully update project role]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
