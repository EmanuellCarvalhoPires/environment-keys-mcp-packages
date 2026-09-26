---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_dashboard
title: "Jira v3 - Get dashboard"
kind: request
request: "[[Jira v3 - Get dashboard]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/dashboard/{id} · Get dashboard. Returns a dashboard. This operation can be accessed anonymously. Permissions required: None. However, to get a dashboard, the dashboard must be shared with the user or the user must own it. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the dashboard."
writes: false
expose: false
---
# jira_get_dashboard

`GET /rest/api/3/dashboard/{id}` — Get dashboard

- Request: [[Jira v3 - Get dashboard]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
