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
path: "/rest/api/3/dashboard/{id}"
category: "Dashboards"
writes_data: true
tool_note: "[[jira_delete_dashboard]]"
---
# Jira v3 - Delete dashboard

**Delete dashboard** — `DELETE /rest/api/3/dashboard/{id}`

- Run by the tool [[jira_delete_dashboard]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/dashboard/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the dashboard.

## Original description

Deletes a dashboard.

**[Permissions](#permissions) required:** None

The dashboard to be deleted must be owned by the user.
