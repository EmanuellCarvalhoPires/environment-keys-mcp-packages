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
path: "/rest/api/3/filter/{id}/favourite"
category: "Filters"
writes_data: true
tool_note: "[[jira_remove_filter_as_favorite]]"
---
# Jira v3 - Remove filter as favorite

**Remove filter as favorite** — `DELETE /rest/api/3/filter/{id}/favourite`

- Run by the tool [[jira_remove_filter_as_favorite]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/filter/{{param:id}}/favourite?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the filter.
- `expand` (query, string, optional) — Use expand to include additional information about filter in the response. This parameter accepts a comma-separated list.

## Original description

Removes a filter as a favorite for the user. Note that this operation only removes filters visible to the user from the user's favorites list. For example, if the user favorites a public filter that is subsequently made private (and is therefore no longer visible on their favorites list) they cannot remove it from their favorites list.

**[Permissions](#permissions) required:** Permission to access Jira.
