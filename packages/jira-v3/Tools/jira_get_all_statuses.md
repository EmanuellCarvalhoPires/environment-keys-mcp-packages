---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-statuses
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_all_statuses
title: "Jira v3 - Get all statuses"
kind: request
request: "[[Jira v3 - Get all statuses]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/status · Get all statuses. Returns a list of all statuses associated with active workflows. This operation can be accessed anonymously. Permissions required: Browse projects project permission for the project. Writes data: no."
writes: false
expose: false
---
# jira_get_all_statuses

`GET /rest/api/3/status` — Get all statuses

- Request: [[Jira v3 - Get all statuses]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
