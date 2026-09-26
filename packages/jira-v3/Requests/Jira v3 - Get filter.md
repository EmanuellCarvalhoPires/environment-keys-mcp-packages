---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/filter/{id}"
category: "Filters"
writes_data: false
tool_note: "[[jira_get_filter]]"
---
# Jira v3 - Get filter

**Get filter** — `GET /rest/api/3/filter/{id}`

- Run by the tool [[jira_get_filter]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/filter/{{param:id}}?expand={{param:expand}}&overrideSharePermissions={{param:overrideSharePermissions}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the filter to return.
- `expand` (query, string, optional) — Use expand to include additional information about filter in the response. This parameter accepts a comma-separated list.
- `overrideSharePermissions` (query, string, optional) — EXPERIMENTAL: Whether share permissions are overridden to enable filters with any share permissions to be returned. Available to users with Administer Jira global permission.

## Original description

Returns a filter.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None, however, the filter is only returned where it is:

 *  owned by the user.
 *  shared with a group that the user is a member of.
 *  shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
 *  shared with a public project.
 *  shared with the public.
