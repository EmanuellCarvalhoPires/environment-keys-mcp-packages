---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-role-actors
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_add_default_actors_to_project_role
title: "Jira v3 - Add default actors to project role"
kind: request
request: "[[Jira v3 - Add default actors to project role]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/role/{id}/actors · Add default actors to project role. Adds default actors to a role. You may add groups or users, but you cannot add groups and users in the same request. Changing a project role's default actors does not affect project role members for projects already created. Writes data: yes."
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
# jira_add_default_actors_to_project_role

`POST /rest/api/3/role/{id}/actors` — Add default actors to project role

- Request: [[Jira v3 - Add default actors to project role]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
