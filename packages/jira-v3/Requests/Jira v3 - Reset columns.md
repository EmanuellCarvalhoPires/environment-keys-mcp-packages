---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/filter/{id}/columns"
category: "Filters"
writes_data: true
tool_note: "[[jira_reset_columns]]"
---
# Jira v3 - Reset columns

**Reset columns** — `DELETE /rest/api/3/filter/{id}/columns`

- Run by the tool [[jira_reset_columns]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/filter/{{param:id}}/columns
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the filter.

## Original description

Reset the user's column configuration for the filter to the default.

**[Permissions](#permissions) required:** Permission to access Jira, however, columns are only reset for:

 *  filters owned by the user.
 *  filters shared with a group that the user is a member of.
 *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
 *  filters shared with a public project.
 *  filters shared with the public.
