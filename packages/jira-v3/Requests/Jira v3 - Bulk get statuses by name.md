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
path: "/rest/api/3/statuses/byNames"
category: "Status"
writes_data: false
tool_note: "[[jira_bulk_get_statuses_by_name]]"
---
# Jira v3 - Bulk get statuses by name

**Bulk get statuses by name** — `GET /rest/api/3/statuses/byNames`

- Run by the tool [[jira_bulk_get_statuses_by_name]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/statuses/byNames?name={{param:name}}&projectId={{param:projectId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `name` (query, string, required) — The list of status names. To include multiple names, provide an ampersand-separated list. For example, name=nameXX&name=nameYY. Min items 1, Max items 50
- `projectId` (query, string, optional) — The project the status is part of or null for global statuses.

## Original description

Returns a list of the statuses specified by one or more status names.

**[Permissions](#permissions) required:**

 *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
 *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)
 *  *Browse projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
