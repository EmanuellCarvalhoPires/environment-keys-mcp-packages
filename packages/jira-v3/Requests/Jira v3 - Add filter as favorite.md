---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/filter/{id}/favourite"
category: "Filters"
writes_data: true
tool_note: "[[jira_add_filter_as_favorite]]"
---
# Jira v3 - Add filter as favorite

**Add filter as favorite** — `PUT /rest/api/3/filter/{id}/favourite`

- Run by the tool [[jira_add_filter_as_favorite]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/filter/{{param:id}}/favourite?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the filter.
- `expand` (query, string, optional) — Use expand to include additional information about filter in the response. This parameter accepts a comma-separated list.

## Original description

Add a filter as a favorite for the user.

**[Permissions](#permissions) required:** Permission to access Jira, however, the user can only favorite:

 *  filters owned by the user.
 *  filters shared with a group that the user is a member of.
 *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
 *  filters shared with a public project.
 *  filters shared with the public.
