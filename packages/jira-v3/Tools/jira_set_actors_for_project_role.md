---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-role-actors
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_set_actors_for_project_role
title: "Jira v3 - Set actors for project role"
kind: request
request: "[[Jira v3 - Set actors for project role]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/project/{projectIdOrKey}/role/{id} · Set actors for project role. Sets the actors for a project role for a project, replacing all existing actors. To add actors to the project without overwriting the existing list, use Add actors to project role. Writes data: yes."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
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
# jira_set_actors_for_project_role

`PUT /rest/api/3/project/{projectIdOrKey}/role/{id}` — Set actors for project role

- Request: [[Jira v3 - Set actors for project role]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
