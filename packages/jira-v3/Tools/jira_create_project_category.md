---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-categories
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_project_category
title: "Jira v3 - Create project category"
kind: request
request: "[[Jira v3 - Create project category]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/projectCategory · Create project category. Creates a project category. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_project_category

`POST /rest/api/3/projectCategory` — Create project category

- Request: [[Jira v3 - Create project category]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
