---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}"
category: "Dashboards"
writes_data: true
tool_note: "[[jira_delete_dashboard_item_property]]"
---
# Jira v3 - Delete dashboard item property

**Delete dashboard item property** — `DELETE /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}`

- Run by the tool [[jira_delete_dashboard_item_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/dashboard/{{param:dashboardId}}/items/{{param:itemId}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
```

## Parameters

- `dashboardId` (path, string, required) — The ID of the dashboard.
- `itemId` (path, string, required) — The ID of the dashboard item.
- `propertyKey` (path, string, required) — The key of the dashboard item property.

## Original description

Deletes a dashboard item property.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** The user must have edit permission of the dashboard.
