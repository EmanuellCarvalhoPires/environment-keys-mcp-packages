---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_update_gadget_on_dashboard
title: "Jira v3 - Update gadget on dashboard"
kind: request
request: "[[Jira v3 - Update gadget on dashboard]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId} · Update gadget on dashboard. Changes the title, position, and color of the gadget on a dashboard. Permissions required: None. Writes data: yes."
params:
  "dashboardId":
    type: string
    required: true
    description: "The ID of the dashboard."
  "gadgetId":
    type: string
    required: true
    description: "The ID of the gadget."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_gadget_on_dashboard

`PUT /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}` — Update gadget on dashboard

- Request: [[Jira v3 - Update gadget on dashboard]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
