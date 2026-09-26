---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-roles
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_project_role_for_project
title: "Jira v3 - Get project role for project"
kind: request
request: "[[Jira v3 - Get project role for project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectIdOrKey}/role/{id} · Get project role for project. Returns a project role's details and actors associated with the project. The list of actors is sorted by display name. To check whether a user belongs to a role based on their group memberships, use Get user with the groups expand parameter selected. Writes data: no."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
  "id":
    type: string
    required: true
    description: "The ID of the project role. Use Get all project roles to get a list of project role IDs."
  "excludeInactiveUsers":
    type: string
    required: false
    description: "Exclude inactive users."
writes: false
expose: false
---
# jira_get_project_role_for_project

`GET /rest/api/3/project/{projectIdOrKey}/role/{id}` — Get project role for project

- Request: [[Jira v3 - Get project role for project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
