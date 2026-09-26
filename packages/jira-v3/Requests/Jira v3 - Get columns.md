---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/filter/{id}/columns"
category: "Filters"
writes_data: false
tool_note: "[[jira_get_columns]]"
---
# Jira v3 - Get columns

**Get columns** — `GET /rest/api/3/filter/{id}/columns`

- Run by the tool [[jira_get_columns]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/filter/{{param:id}}/columns
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the filter.

## Original description

Returns the columns configured for a filter. The column configuration is used when the filter's results are viewed in *List View* with the *Columns* set to *Filter*.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None, however, column details are only returned for:

 *  filters owned by the user.
 *  filters shared with a group that the user is a member of.
 *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
 *  filters shared with a public project.
 *  filters shared with the public.
