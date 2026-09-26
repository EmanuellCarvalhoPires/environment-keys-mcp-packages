---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/time-tracking
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_selected_time_tracking_provider
title: "Jira v3 - Get selected time tracking provider"
kind: request
request: "[[Jira v3 - Get selected time tracking provider]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/configuration/timetracking · Get selected time tracking provider. Returns the time tracking provider that is currently selected. Note that if time tracking is disabled, then a successful but empty response is returned. Permissions required: Administer Jira global permission. Writes data: no."
writes: false
expose: false
---
# jira_get_selected_time_tracking_provider

`GET /rest/api/3/configuration/timetracking` — Get selected time tracking provider

- Request: [[Jira v3 - Get selected time tracking provider]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
