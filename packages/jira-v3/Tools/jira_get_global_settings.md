---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/jira-settings
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_global_settings
title: "Jira v3 - Get global settings"
kind: request
request: "[[Jira v3 - Get global settings]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/configuration · Get global settings. Returns the global settings in Jira. These settings determine whether optional features (for example, subtasks, time tracking, and others) are enabled. If time tracking is enabled, this operation also returns the time tracking configuration. Writes data: no."
writes: false
expose: false
---
# jira_get_global_settings

`GET /rest/api/3/configuration` — Get global settings

- Request: [[Jira v3 - Get global settings]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
