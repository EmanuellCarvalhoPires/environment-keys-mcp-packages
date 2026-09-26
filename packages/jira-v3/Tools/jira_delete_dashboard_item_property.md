---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_delete_dashboard_item_property
title: "Jira v3 - Delete dashboard item property"
kind: request
request: "[[Jira v3 - Delete dashboard item property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey} · Delete dashboard item property. Deletes a dashboard item property. This operation can be accessed anonymously. Permissions required: The user must have edit permission of the dashboard. Writes data: yes."
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
writes: true
expose: false
---
# jira_delete_dashboard_item_property

`DELETE /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}` — Delete dashboard item property

- Request: [[Jira v3 - Delete dashboard item property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
