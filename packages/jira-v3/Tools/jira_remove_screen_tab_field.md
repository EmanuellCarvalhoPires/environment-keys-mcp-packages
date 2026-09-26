---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-tab-fields
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_remove_screen_tab_field
title: "Jira v3 - Remove screen tab field"
kind: request
request: "[[Jira v3 - Remove screen tab field]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id} · Remove screen tab field. Removes a field from a screen tab. Permissions required: Administer Jira global permission. Writes data: yes."
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
writes: true
expose: false
---
# jira_remove_screen_tab_field

`DELETE /rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}` — Remove screen tab field

- Request: [[Jira v3 - Remove screen tab field]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
