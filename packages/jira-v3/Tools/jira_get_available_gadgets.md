---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_available_gadgets
title: "Jira v3 - Get available gadgets"
kind: request
request: "[[Jira v3 - Get available gadgets]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/dashboard/gadgets · Get available gadgets. Gets a list of all available gadgets that can be added to all dashboards. Permissions required: None. Writes data: no."
writes: false
expose: false
---
# jira_get_available_gadgets

`GET /rest/api/3/dashboard/gadgets` — Get available gadgets

- Request: [[Jira v3 - Get available gadgets]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
