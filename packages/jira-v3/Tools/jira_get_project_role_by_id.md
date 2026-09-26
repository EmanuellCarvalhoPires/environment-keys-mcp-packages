---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-roles
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_project_role_by_id
title: "Jira v3 - Get project role by ID"
kind: request
request: "[[Jira v3 - Get project role by ID]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/role/{id} · Get project role by ID. Gets the project role details and the default actors associated with the role. The list of default actors is sorted by display name. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the project role. Use Get all project roles to get a list of project role IDs."
writes: false
expose: false
---
# jira_get_project_role_by_id

`GET /rest/api/3/role/{id}` — Get project role by ID

- Request: [[Jira v3 - Get project role by ID]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
