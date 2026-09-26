---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-tabs
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_screen_tab
title: "Jira v3 - Update screen tab"
kind: request
request: "[[Jira v3 - Update screen tab]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/screens/{screenId}/tabs/{tabId} · Update screen tab. Updates the name of a screen tab. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "screenId":
    type: string
    required: true
    description: "The ID of the screen."
  "tabId":
    type: string
    required: true
    description: "The ID of the screen tab."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_screen_tab

`PUT /rest/api/3/screens/{screenId}/tabs/{tabId}` — Update screen tab

- Request: [[Jira v3 - Update screen tab]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
