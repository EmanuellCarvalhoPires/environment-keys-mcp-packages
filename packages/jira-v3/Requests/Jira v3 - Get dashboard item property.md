---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}"
category: "Dashboards"
writes_data: false
tool_note: "[[jira_get_dashboard_item_property]]"
---
# Jira v3 - Get dashboard item property

**Get dashboard item property** — `GET /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}`

- Run by the tool [[jira_get_dashboard_item_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/dashboard/{{param:dashboardId}}/items/{{param:itemId}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `dashboardId` (path, string, required) — The ID of the dashboard.
- `itemId` (path, string, required) — The ID of the dashboard item.
- `propertyKey` (path, string, required) — The key of the dashboard item property.

## Original description

Returns the key and value of a dashboard item property.

A dashboard item enables an app to add user-specific information to a user dashboard. Dashboard items are exposed to users as gadgets that users can add to their dashboards. For more information on how users do this, see [Adding and customizing gadgets](https://confluence.atlassian.com/x/7AeiLQ).

When an app creates a dashboard item it registers a callback to receive the dashboard item ID. The callback fires whenever the item is rendered or, where the item is configurable, the user edits the item. The app then uses this resource to store the item's content or configuration details. For more information on working with dashboard items, see [ Building a dashboard item for a JIRA Connect add-on](https://developer.atlassian.com/server/jira/platform/guide-building-a-dashboard-item-for-a-jira-connect-add-on-33746254/) and the [Dashboard Item](https://developer.atlassian.com/cloud/jira/platform/modules/dashboard-item/) documentation.

There is no resource to set or get dashboard items.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** The user must have read permission of the dashboard or have the dashboard shared with them.
