---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-tabs
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_move_screen_tab
title: "Jira v3 - Move screen tab"
kind: request
request: "[[Jira v3 - Move screen tab]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/screens/{screenId}/tabs/{tabId}/move/{pos} · Move screen tab. Moves a screen tab. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "screenId":
    type: string
    required: true
    description: "The ID of the screen."
  "tabId":
    type: string
    required: true
    description: "The ID of the screen tab."
  "pos":
    type: string
    required: true
    description: "The position of tab. The base index is 0."
writes: true
expose: false
---
# jira_move_screen_tab

`POST /rest/api/3/screens/{screenId}/tabs/{tabId}/move/{pos}` — Move screen tab

- Request: [[Jira v3 - Move screen tab]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
