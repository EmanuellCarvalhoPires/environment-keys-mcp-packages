---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-roles
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_project_role
title: "Jira v3 - Create project role"
kind: request
request: "[[Jira v3 - Create project role]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/role · Create project role. Creates a new project role with no default actors. You can use the Add default actors to project role operation to add default actors to the project role after creating it. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_project_role

`POST /rest/api/3/role` — Create project role

- Request: [[Jira v3 - Create project role]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
