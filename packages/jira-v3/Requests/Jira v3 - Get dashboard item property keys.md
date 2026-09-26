---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties"
category: "Dashboards"
writes_data: false
tool_note: "[[jira_get_dashboard_item_property_keys]]"
---
# Jira v3 - Get dashboard item property keys

**Get dashboard item property keys** — `GET /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties`

- Run by the tool [[jira_get_dashboard_item_property_keys]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/dashboard/{{param:dashboardId}}/items/{{param:itemId}}/properties
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `dashboardId` (path, string, required) — The ID of the dashboard.
- `itemId` (path, string, required) — The ID of the dashboard item.

## Original description

Returns the keys of all properties for a dashboard item.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** The user must have read permission of the dashboard or have the dashboard shared with them.
