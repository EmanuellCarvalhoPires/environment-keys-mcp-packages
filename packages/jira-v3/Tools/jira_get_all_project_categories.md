---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-categories
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_all_project_categories
title: "Jira v3 - Get all project categories"
kind: request
request: "[[Jira v3 - Get all project categories]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/projectCategory · Get all project categories. Returns all project categories. Permissions required: Permission to access Jira. Writes data: no."
writes: false
expose: false
---
# jira_get_all_project_categories

`GET /rest/api/3/projectCategory` — Get all project categories

- Request: [[Jira v3 - Get all project categories]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
