---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_copy_dashboard
title: "Jira v3 - Copy dashboard"
kind: request
request: "[[Jira v3 - Copy dashboard]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/dashboard/{id}/copy · Copy dashboard. Copies a dashboard. Any values provided in the dashboard parameter replace those in the copied dashboard. Permissions required: None The dashboard to be copied must be owned by or shared with the user. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
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
# jira_copy_dashboard

`POST /rest/api/3/dashboard/{id}/copy` — Copy dashboard

- Request: [[Jira v3 - Copy dashboard]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
