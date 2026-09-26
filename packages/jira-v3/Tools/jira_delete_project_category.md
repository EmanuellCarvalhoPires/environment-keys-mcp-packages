---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-categories
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_project_category
title: "Jira v3 - Delete project category"
kind: request
request: "[[Jira v3 - Delete project category]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/projectCategory/{id} · Delete project category. Deletes a project category. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "ID of the project category to delete."
writes: true
expose: false
---
# jira_delete_project_category

`DELETE /rest/api/3/projectCategory/{id}` — Delete project category

- Request: [[Jira v3 - Delete project category]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
