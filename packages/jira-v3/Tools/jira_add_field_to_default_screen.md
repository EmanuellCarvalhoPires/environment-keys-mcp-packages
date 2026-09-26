---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/screens
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_add_field_to_default_screen
title: "Jira v3 - Add field to default screen"
kind: request
request: "[[Jira v3 - Add field to default screen]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/screens/addToDefault/{fieldId} · Add field to default screen. Adds a field to the default tab of the default screen. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "fieldId":
    type: string
    required: true
    description: "The ID of the field."
writes: true
expose: false
---
# jira_add_field_to_default_screen

`POST /rest/api/3/screens/addToDefault/{fieldId}` — Add field to default screen

- Request: [[Jira v3 - Add field to default screen]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
