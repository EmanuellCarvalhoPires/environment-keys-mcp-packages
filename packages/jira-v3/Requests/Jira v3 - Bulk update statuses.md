---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/status
  - api/operation/update
  - api/effect/write
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/statuses"
category: "Status"
writes_data: true
tool_note: "[[jira_bulk_update_statuses]]"
---
# Jira v3 - Bulk update statuses

**Bulk update statuses** — `PUT /rest/api/3/statuses`

- Run by the tool [[jira_bulk_update_statuses]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/statuses
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "statuses": [
    {
      "description": "The issue is resolved",
      "id": "1000",
      "name": "Finished",
      "statusCategory": "DONE"
    }
  ]
}
```

## Original description

Updates statuses by ID.

**[Permissions](#permissions) required:**

 *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
 *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)
