---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_remove_gadget_from_dashboard
title: "Jira v3 - Remove gadget from dashboard"
kind: request
request: "[[Jira v3 - Remove gadget from dashboard]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId} · Remove gadget from dashboard. Removes a dashboard gadget from a dashboard. When a gadget is removed from a dashboard, other gadgets in the same column are moved up to fill the emptied position. Permissions required: None. Writes data: yes."
params:
  "dashboardId":
    type: string
    required: true
    description: "The ID of the dashboard."
  "gadgetId":
    type: string
    required: true
    description: "The ID of the gadget."
writes: true
expose: false
---
# jira_remove_gadget_from_dashboard

`DELETE /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}` — Remove gadget from dashboard

- Request: [[Jira v3 - Remove gadget from dashboard]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
