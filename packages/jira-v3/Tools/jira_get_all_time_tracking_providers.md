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
tool: jira_get_all_time_tracking_providers
title: "Jira v3 - Get all time tracking providers"
kind: request
request: "[[Jira v3 - Get all time tracking providers]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/configuration/timetracking/list · Get all time tracking providers. Returns all time tracking providers. By default, Jira only has one time tracking provider: JIRA provided time tracking. However, you can install other time tracking providers via apps from the Atlassian Marketplace. Writes data: no."
writes: false
expose: false
---
# jira_get_all_time_tracking_providers

`GET /rest/api/3/configuration/timetracking/list` — Get all time tracking providers

- Request: [[Jira v3 - Get all time tracking providers]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
