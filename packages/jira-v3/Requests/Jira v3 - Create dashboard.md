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
path: "/rest/api/3/dashboard"
category: "Dashboards"
writes_data: true
tool_note: "[[jira_create_dashboard]]"
---
# Jira v3 - Create dashboard

**Create dashboard** — `POST /rest/api/3/dashboard`

- Run by the tool [[jira_create_dashboard]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/dashboard?extendAdminPermissions={{param:extendAdminPermissions}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

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

Creates a dashboard.

**[Permissions](#permissions) required:** None.
