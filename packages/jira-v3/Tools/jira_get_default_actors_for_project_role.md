---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-role-actors
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_default_actors_for_project_role
title: "Jira v3 - Get default actors for project role"
kind: request
request: "[[Jira v3 - Get default actors for project role]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/role/{id}/actors · Get default actors for project role. Returns the default actors for the project role. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the project role. Use Get all project roles to get a list of project role IDs."
writes: false
expose: false
---
# jira_get_default_actors_for_project_role

`GET /rest/api/3/role/{id}/actors` — Get default actors for project role

- Request: [[Jira v3 - Get default actors for project role]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
