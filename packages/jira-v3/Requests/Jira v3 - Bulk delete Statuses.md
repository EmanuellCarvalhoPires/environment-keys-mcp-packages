---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/status
  - api/operation/delete
  - api/effect/write
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/statuses"
category: "Status"
writes_data: true
tool_note: "[[jira_bulk_delete_statuses]]"
---
# Jira v3 - Bulk delete Statuses

**Bulk delete Statuses** — `DELETE /rest/api/3/statuses`

- Run by the tool [[jira_bulk_delete_statuses]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/statuses?id={{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (query, string, required) — The list of status IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001. Min items 1, Max items 50

## Original description

Deletes statuses by ID.

**[Permissions](#permissions) required:**

 *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
 *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)
