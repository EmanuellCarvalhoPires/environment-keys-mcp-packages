---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-categories
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_project_category_by_id
title: "Jira v3 - Get project category by ID"
kind: request
request: "[[Jira v3 - Get project category by ID]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/projectCategory/{id} · Get project category by ID. Returns a project category. Permissions required: Permission to access Jira. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the project category."
writes: false
expose: false
---
# jira_get_project_category_by_id

`GET /rest/api/3/projectCategory/{id}` — Get project category by ID

- Request: [[Jira v3 - Get project category by ID]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
