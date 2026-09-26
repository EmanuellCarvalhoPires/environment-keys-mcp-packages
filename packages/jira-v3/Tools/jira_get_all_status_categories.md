---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-status-categories
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_all_status_categories
title: "Jira v3 - Get all status categories"
kind: request
request: "[[Jira v3 - Get all status categories]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/statuscategory · Get all status categories. Returns a list of all status categories. Permissions required: Permission to access Jira. Writes data: no."
writes: false
expose: false
---
# jira_get_all_status_categories

`GET /rest/api/3/statuscategory` — Get all status categories

- Request: [[Jira v3 - Get all status categories]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
