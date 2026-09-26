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
path: "/rest/api/3/filter/favourite"
category: "Filters"
writes_data: false
tool_note: "[[jira_get_favorite_filters]]"
---
# Jira v3 - Get favorite filters

**Get favorite filters** — `GET /rest/api/3/filter/favourite`

- Run by the tool [[jira_get_favorite_filters]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/filter/favourite?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `expand` (query, string, optional) — Use expand to include additional information about filter in the response. This parameter accepts a comma-separated list.

## Original description

Returns the visible favorite filters of the user.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** A favorite filter is only visible to the user where the filter is:

 *  owned by the user.
 *  shared with a group that the user is a member of.
 *  shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
 *  shared with a public project.
 *  shared with the public.

For example, if the user favorites a public filter that is subsequently made private that filter is not returned by this operation.
