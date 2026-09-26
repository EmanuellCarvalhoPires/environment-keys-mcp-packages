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
tool: jira_create_screen
title: "Jira v3 - Create screen"
kind: request
request: "[[Jira v3 - Create screen]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/screens · Create screen. Creates a screen with a default field tab. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_screen

`POST /rest/api/3/screens` — Create screen

- Request: [[Jira v3 - Create screen]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
