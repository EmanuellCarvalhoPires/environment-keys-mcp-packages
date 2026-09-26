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
path: "/rest/api/3/dashboard/bulk/edit"
category: "Dashboards"
writes_data: true
tool_note: "[[jira_bulk_edit_dashboards]]"
---
# Jira v3 - Bulk edit dashboards

**Bulk edit dashboards** — `PUT /rest/api/3/dashboard/bulk/edit`

- Run by the tool [[jira_bulk_edit_dashboards]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/dashboard/bulk/edit
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "action": "changePermission",
  "entityIds": [
    10001,
    10002
  ],
  "extendAdminPermissions": true,
  "permissionDetails": {
    "editPermissions": [
      {
        "group": {
          "groupId": "276f955c-63d7-42c8-9520-92d01dca0625",
          "name": "jira-administrators",
          "self": "https://your-domain.atlassian.net/rest/api/~ver~/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625"
        },
        "id": 10010,
        "type": "group"
      }
    ],
    "sharePermissions": [
      {
        "id": 10000,
        "type": "global"
      }
    ]
  }
}
```

## Original description

Bulk edit dashboards. Maximum number of dashboards to be edited at the same time is 100.

**[Permissions](#permissions) required:** None

The dashboards to be updated must be owned by the user, or the user must be an administrator.
