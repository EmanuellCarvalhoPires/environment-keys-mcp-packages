---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_set_dashboard_item_property
title: "Jira v3 - Set dashboard item property"
kind: request
request: "[[Jira v3 - Set dashboard item property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey} · Set dashboard item property. Sets the value of a dashboard item property. Use this resource in apps to store custom data against a dashboard item. A dashboard item enables an app to add user-specific information to a user dashboard. Writes data: yes."
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
    description: "The key of the dashboard item property. The maximum length is 255 characters. For dashboard items with a spec URI and no complete module key, if the provided propertyKey is equal to \"config\", the requ…"
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_dashboard_item_property

`PUT /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}` — Set dashboard item property

- Request: [[Jira v3 - Set dashboard item property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
