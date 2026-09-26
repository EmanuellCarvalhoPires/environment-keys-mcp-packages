---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-roles
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_project_roles_for_project
title: "Jira v3 - Get project roles for project"
kind: request
request: "[[Jira v3 - Get project roles for project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectIdOrKey}/role · Get project roles for project. Returns a list of project roles for the project returning the name and self URL for each role. Note that all project roles are shared with all projects in Jira Cloud. See Get all project roles for more information. This operation can be accessed anonymously. Writes data: no."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
writes: false
expose: false
---
# jira_get_project_roles_for_project

`GET /rest/api/3/project/{projectIdOrKey}/role` — Get project roles for project

- Request: [[Jira v3 - Get project roles for project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
