---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-tab-fields
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_move_screen_tab_field
title: "Jira v3 - Move screen tab field"
kind: request
request: "[[Jira v3 - Move screen tab field]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}/move · Move screen tab field. Moves a screen tab field. If after and position are provided in the request, position is ignored. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "screenId":
    type: string
    required: true
    description: "The ID of the screen."
  "tabId":
    type: string
    required: true
    description: "The ID of the screen tab."
  "id":
    type: string
    required: true
    description: "The ID of the field."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_move_screen_tab_field

`POST /rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}/move` — Move screen tab field

- Request: [[Jira v3 - Move screen tab field]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
