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
tool: jira_get_time_tracking_settings
title: "Jira v3 - Get time tracking settings"
kind: request
request: "[[Jira v3 - Get time tracking settings]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/configuration/timetracking/options · Get time tracking settings. Returns the time tracking settings. This includes settings such as the time format, default time unit, and others. For more information, see Configuring time tracking. Permissions required: Administer Jira global permission. Writes data: no."
writes: false
expose: false
---
# jira_get_time_tracking_settings

`GET /rest/api/3/configuration/timetracking/options` — Get time tracking settings

- Request: [[Jira v3 - Get time tracking settings]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
