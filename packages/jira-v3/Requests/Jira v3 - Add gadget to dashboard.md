---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/dashboard/{dashboardId}/gadget"
category: "Dashboards"
writes_data: true
tool_note: "[[jira_add_gadget_to_dashboard]]"
---
# Jira v3 - Add gadget to dashboard

**Add gadget to dashboard** — `POST /rest/api/3/dashboard/{dashboardId}/gadget`

- Run by the tool [[jira_add_gadget_to_dashboard]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/dashboard/{{param:dashboardId}}/gadget
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `dashboardId` (path, string, required) — The ID of the dashboard.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "color": "blue",
  "ignoreUriAndModuleKeyValidation": false,
  "moduleKey": "com.atlassian.plugins.atlassian-connect-plugin:com.atlassian.connect.node.sample-addon__sample-dashboard-item",
  "position": {
    "column": 1,
    "row": 0
  },
  "title": "Issue statistics"
}
```

## Original description

Adds a gadget to a dashboard.

**[Permissions](#permissions) required:** None.
