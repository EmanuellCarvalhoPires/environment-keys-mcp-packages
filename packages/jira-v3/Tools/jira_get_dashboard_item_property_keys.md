---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_dashboard_item_property_keys
title: "Jira v3 - Get dashboard item property keys"
kind: request
request: "[[Jira v3 - Get dashboard item property keys]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties · Get dashboard item property keys. Returns the keys of all properties for a dashboard item. This operation can be accessed anonymously. Permissions required: The user must have read permission of the dashboard or have the dashboard shared with them. Writes data: no."
params:
  "dashboardId":
    type: string
    required: true
    description: "The ID of the dashboard."
  "itemId":
    type: string
    required: true
    description: "The ID of the dashboard item."
writes: false
expose: false
---
# jira_get_dashboard_item_property_keys

`GET /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties` — Get dashboard item property keys

- Request: [[Jira v3 - Get dashboard item property keys]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
