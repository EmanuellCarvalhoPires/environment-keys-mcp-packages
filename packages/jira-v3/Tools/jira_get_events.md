---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_events
title: "Jira v3 - Get events"
kind: request
request: "[[Jira v3 - Get events]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/events · Get events. Returns all issue events. Permissions required: Administer Jira global permission. Writes data: no."
writes: false
expose: false
---
# jira_get_events

`GET /rest/api/3/events` — Get events

- Request: [[Jira v3 - Get events]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
