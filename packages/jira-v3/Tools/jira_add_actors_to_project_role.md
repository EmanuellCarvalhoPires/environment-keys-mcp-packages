---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-role-actors
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_add_actors_to_project_role
title: "Jira v3 - Add actors to project role"
kind: request
request: "[[Jira v3 - Add actors to project role]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/project/{projectIdOrKey}/role/{id} · Add actors to project role. Adds actors to a project role for the project. To replace all actors for the project, use Set actors for project role. This operation can be accessed anonymously. Permissions required: Administer Projects project permission for the project or Administer Jira global permission. Writes data: yes."
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
# jira_add_actors_to_project_role

`POST /rest/api/3/project/{projectIdOrKey}/role/{id}` — Add actors to project role

- Request: [[Jira v3 - Add actors to project role]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
