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
tool: jira_select_time_tracking_provider
title: "Jira v3 - Select time tracking provider"
kind: request
request: "[[Jira v3 - Select time tracking provider]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/configuration/timetracking · Select time tracking provider. Selects a time tracking provider. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_select_time_tracking_provider

`PUT /rest/api/3/configuration/timetracking` — Select time tracking provider

- Request: [[Jira v3 - Select time tracking provider]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
