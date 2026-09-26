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
path: "/rest/api/3/dashboard/{id}"
category: "Dashboards"
writes_data: true
tool_note: "[[jira_update_dashboard]]"
---
# Jira v3 - Update dashboard

**Update dashboard** — `PUT /rest/api/3/dashboard/{id}`

- Run by the tool [[jira_update_dashboard]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/dashboard/{{param:id}}?extendAdminPermissions={{param:extendAdminPermissions}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the dashboard to update.
- `extendAdminPermissions` (query, string, optional) — Whether admin level permissions are used. It should only be true if the user has Administer Jira global permission
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "A dashboard to help auditors identify sample of issues to check.",
  "editPermissions": [],
  "name": "Auditors dashboard",
  "sharePermissions": [
    {
      "type": "global"
    }
  ]
}
```

## Original description

Updates a dashboard, replacing all the dashboard details with those provided.

**[Permissions](#permissions) required:** None

The dashboard to be updated must be owned by the user.
