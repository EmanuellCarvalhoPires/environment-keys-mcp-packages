---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/screens
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_screen
title: "Jira v3 - Update screen"
kind: request
request: "[[Jira v3 - Update screen]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/screens/{screenId} · Update screen. Updates a screen. Only screens used in classic projects can be updated. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "screenId":
    type: string
    required: true
    description: "The ID of the screen."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_screen

`PUT /rest/api/3/screens/{screenId}` — Update screen

- Request: [[Jira v3 - Update screen]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
