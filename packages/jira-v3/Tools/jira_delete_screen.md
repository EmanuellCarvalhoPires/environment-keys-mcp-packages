---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/screens
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_delete_screen
title: "Jira v3 - Delete screen"
kind: request
request: "[[Jira v3 - Delete screen]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/screens/{screenId} · Delete screen. Deletes a screen. A screen cannot be deleted if it is used in a screen scheme, workflow, or workflow draft. Only screens used in classic projects can be deleted. Writes data: yes."
params:
  "screenId":
    type: string
    required: true
    description: "The ID of the screen."
writes: true
expose: false
---
# jira_delete_screen

`DELETE /rest/api/3/screens/{screenId}` — Delete screen

- Request: [[Jira v3 - Delete screen]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
