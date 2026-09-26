---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-tabs
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_screen_tab
title: "Jira v3 - Create screen tab"
kind: request
request: "[[Jira v3 - Create screen tab]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/screens/{screenId}/tabs · Create screen tab. Creates a tab for a screen. Permissions required: Administer Jira global permission. Writes data: yes."
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
# jira_create_screen_tab

`POST /rest/api/3/screens/{screenId}/tabs` — Create screen tab

- Request: [[Jira v3 - Create screen tab]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
