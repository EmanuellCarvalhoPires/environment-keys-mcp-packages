---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/dashboard/{id}"
category: "Dashboards"
writes_data: false
tool_note: "[[jira_get_dashboard]]"
---
# Jira v3 - Get dashboard

**Get dashboard** — `GET /rest/api/3/dashboard/{id}`

- Run by the tool [[jira_get_dashboard]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/dashboard/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the dashboard.

## Original description

Returns a dashboard.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.

However, to get a dashboard, the dashboard must be shared with the user or the user must own it. Note, users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System dashboard. The System dashboard is considered to be shared with all other users.
