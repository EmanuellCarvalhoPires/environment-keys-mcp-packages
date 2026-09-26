---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/filter/{id}"
category: "Filters"
writes_data: true
tool_note: "[[jira_delete_filter]]"
---
# Jira v3 - Delete filter

**Delete filter** — `DELETE /rest/api/3/filter/{id}`

- Run by the tool [[jira_delete_filter]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/filter/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the filter to delete.

## Original description

Delete a filter.

**[Permissions](#permissions) required:** Permission to access Jira, however filters can only be deleted by the creator of the filter or a user with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
