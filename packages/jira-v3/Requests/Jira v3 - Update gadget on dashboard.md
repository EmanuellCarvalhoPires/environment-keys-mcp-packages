---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}"
category: "Dashboards"
writes_data: true
tool_note: "[[jira_update_gadget_on_dashboard]]"
---
# Jira v3 - Update gadget on dashboard

**Update gadget on dashboard** — `PUT /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}`

- Run by the tool [[jira_update_gadget_on_dashboard]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/dashboard/{{param:dashboardId}}/gadget/{{param:gadgetId}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `dashboardId` (path, string, required) — The ID of the dashboard.
- `gadgetId` (path, string, required) — The ID of the gadget.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "color": "red",
  "position": {
    "column": 1,
    "row": 1
  },
  "title": "My new gadget title"
}
```

## Original description

Changes the title, position, and color of the gadget on a dashboard.

**[Permissions](#permissions) required:** None.
