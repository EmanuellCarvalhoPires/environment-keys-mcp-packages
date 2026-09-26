---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/status
  - api/operation/list
  - api/effect/read
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/statuses"
category: "Status"
writes_data: false
tool_note: "[[jira_bulk_get_statuses]]"
---
# Jira v3 - Bulk get statuses

**Bulk get statuses** — `GET /rest/api/3/statuses`

- Run by the tool [[jira_bulk_get_statuses]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/statuses?id={{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (query, string, required) — The list of status IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001. Min items 1, Max items 50

## Original description

Returns a list of the statuses specified by one or more status IDs.

**[Permissions](#permissions) required:**

 *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
 *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)
