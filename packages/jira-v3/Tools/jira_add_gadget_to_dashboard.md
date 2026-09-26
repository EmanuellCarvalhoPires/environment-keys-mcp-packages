---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_add_gadget_to_dashboard
title: "Jira v3 - Add gadget to dashboard"
kind: request
request: "[[Jira v3 - Add gadget to dashboard]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/dashboard/{dashboardId}/gadget · Add gadget to dashboard. Adds a gadget to a dashboard. Permissions required: None. Writes data: yes."
params:
  "dashboardId":
    type: string
    required: true
    description: "The ID of the dashboard."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_add_gadget_to_dashboard

`POST /rest/api/3/dashboard/{dashboardId}/gadget` — Add gadget to dashboard

- Request: [[Jira v3 - Add gadget to dashboard]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
