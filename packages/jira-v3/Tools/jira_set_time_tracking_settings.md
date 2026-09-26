---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/time-tracking
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_set_time_tracking_settings
title: "Jira v3 - Set time tracking settings"
kind: request
request: "[[Jira v3 - Set time tracking settings]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/configuration/timetracking/options · Set time tracking settings. Sets the time tracking settings. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_time_tracking_settings

`PUT /rest/api/3/configuration/timetracking/options` — Set time tracking settings

- Request: [[Jira v3 - Set time tracking settings]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
