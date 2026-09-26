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
path: "/rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}"
category: "Dashboards"
writes_data: true
tool_note: "[[jira_remove_gadget_from_dashboard]]"
---
# Jira v3 - Remove gadget from dashboard

**Remove gadget from dashboard** — `DELETE /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}`

- Run by the tool [[jira_remove_gadget_from_dashboard]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/dashboard/{{param:dashboardId}}/gadget/{{param:gadgetId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `dashboardId` (path, string, required) — The ID of the dashboard.
- `gadgetId` (path, string, required) — The ID of the gadget.

## Original description

Removes a dashboard gadget from a dashboard.

When a gadget is removed from a dashboard, other gadgets in the same column are moved up to fill the emptied position.

**[Permissions](#permissions) required:** None.
