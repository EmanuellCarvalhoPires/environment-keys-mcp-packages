---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/filter-sharing
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/filter/{id}/permission"
category: "Filter sharing"
writes_data: false
tool_note: "[[jira_get_share_permissions]]"
---
# Jira v3 - Get share permissions

**Get share permissions** — `GET /rest/api/3/filter/{id}/permission`

- Run by the tool [[jira_get_share_permissions]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/filter/{{param:id}}/permission
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the filter.

## Original description

Returns the share permissions for a filter. A filter can be shared with groups, projects, all logged-in users, or the public. Sharing with all logged-in users or the public is known as a global share permission.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None, however, share permissions are only returned for:

 *  filters owned by the user.
 *  filters shared with a group that the user is a member of.
 *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
 *  filters shared with a public project.
 *  filters shared with the public.
