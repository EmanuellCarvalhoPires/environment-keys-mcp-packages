---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_dashboard_item_property
title: "Jira v3 - Get dashboard item property"
kind: request
request: "[[Jira v3 - Get dashboard item property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey} · Get dashboard item property. Returns the key and value of a dashboard item property. A dashboard item enables an app to add user-specific information to a user dashboard. Dashboard items are exposed to users as gadgets that users can add to their dashboards. Writes data: no."
params:
  "dashboardId":
    type: string
    required: true
    description: "The ID of the dashboard."
  "itemId":
    type: string
    required: true
    description: "The ID of the dashboard item."
  "propertyKey":
    type: string
    required: true
    description: "The key of the dashboard item property."
writes: false
expose: false
---
# jira_get_dashboard_item_property

`GET /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}` — Get dashboard item property

- Request: [[Jira v3 - Get dashboard item property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
