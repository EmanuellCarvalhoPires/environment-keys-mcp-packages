---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/status
  - api/operation/action
  - api/effect/write
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/statuses"
category: "Status"
writes_data: true
tool_note: "[[jira_bulk_create_statuses]]"
---
# Jira v3 - Bulk create statuses

**Bulk create statuses** — `POST /rest/api/3/statuses`

- Run by the tool [[jira_bulk_create_statuses]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/statuses
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
  "scope": {
    "project": {
      "id": "1"
    },
    "type": "PROJECT"
  },
  "statuses": [
    {
      "description": "The issue is resolved",
      "name": "Finished",
      "statusCategory": "DONE"
    }
  ]
}
```

## Original description

Creates statuses for a global or project scope.

**[Permissions](#permissions) required:**

 *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
 *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)
