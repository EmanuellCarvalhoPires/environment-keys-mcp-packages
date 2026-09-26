---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/screens
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_available_screen_fields
title: "Jira v3 - Get available screen fields"
kind: request
request: "[[Jira v3 - Get available screen fields]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/screens/{screenId}/availableFields · Get available screen fields. Returns the fields that can be added to a tab on a screen. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "screenId":
    type: string
    required: true
    description: "The ID of the screen."
writes: false
expose: false
---
# jira_get_available_screen_fields

`GET /rest/api/3/screens/{screenId}/availableFields` — Get available screen fields

- Request: [[Jira v3 - Get available screen fields]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
