---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-roles
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_all_project_roles
title: "Jira v3 - Get all project roles"
kind: request
request: "[[Jira v3 - Get all project roles]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/role · Get all project roles. Gets a list of all project roles, complete with project role details and default actors. About project roles Project roles are a flexible way to to associate users and groups with projects. Writes data: no."
writes: false
expose: false
---
# jira_get_all_project_roles

`GET /rest/api/3/role` — Get all project roles

- Request: [[Jira v3 - Get all project roles]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
