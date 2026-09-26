---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-categories
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_project_category
title: "Jira v3 - Update project category"
kind: request
request: "[[Jira v3 - Update project category]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/projectCategory/{id} · Update project category. Updates a project category. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_project_category

`PUT /rest/api/3/projectCategory/{id}` — Update project category

- Request: [[Jira v3 - Update project category]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
