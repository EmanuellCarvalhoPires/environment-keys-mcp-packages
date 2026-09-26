---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_create_dashboard
title: "Jira v3 - Create dashboard"
kind: request
request: "[[Jira v3 - Create dashboard]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/dashboard · Create dashboard. Creates a dashboard. Permissions required: None. Writes data: yes."
params:
  "extendAdminPermissions":
    type: string
    required: false
    description: "Whether admin level permissions are used. It should only be true if the user has Administer Jira global permission"
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_dashboard

`POST /rest/api/3/dashboard` — Create dashboard

- Request: [[Jira v3 - Create dashboard]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
