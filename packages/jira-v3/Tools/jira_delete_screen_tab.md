---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-tabs
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_screen_tab
title: "Jira v3 - Delete screen tab"
kind: request
request: "[[Jira v3 - Delete screen tab]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/screens/{screenId}/tabs/{tabId} · Delete screen tab. Deletes a screen tab. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "screenId":
    type: string
    required: true
    description: "The ID of the screen."
  "tabId":
    type: string
    required: true
    description: "The ID of the screen tab."
writes: true
expose: false
---
# jira_delete_screen_tab

`DELETE /rest/api/3/screens/{screenId}/tabs/{tabId}` — Delete screen tab

- Request: [[Jira v3 - Delete screen tab]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
