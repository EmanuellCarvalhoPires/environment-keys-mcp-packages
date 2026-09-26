---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_update_dashboard
title: "Jira v3 - Update dashboard"
kind: request
request: "[[Jira v3 - Update dashboard]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/dashboard/{id} · Update dashboard. Updates a dashboard, replacing all the dashboard details with those provided. Permissions required: None The dashboard to be updated must be owned by the user. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the dashboard to update."
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
# jira_update_dashboard

`PUT /rest/api/3/dashboard/{id}` — Update dashboard

- Request: [[Jira v3 - Update dashboard]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
