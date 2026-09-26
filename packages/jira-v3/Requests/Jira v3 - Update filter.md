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
path: "/rest/api/3/filter/{id}"
category: "Filters"
writes_data: true
tool_note: "[[jira_update_filter]]"
---
# Jira v3 - Update filter

**Update filter** — `PUT /rest/api/3/filter/{id}`

- Run by the tool [[jira_update_filter]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/filter/{{param:id}}?expand={{param:expand}}&overrideSharePermissions={{param:overrideSharePermissions}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the filter to update.
- `expand` (query, string, optional) — Use expand to include additional information about filter in the response. This parameter accepts a comma-separated list.
- `overrideSharePermissions` (query, string, optional) — EXPERIMENTAL: Whether share permissions are overridden to enable the addition of any share permissions to filters. Available to users with Administer Jira global permission.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "Lists all open bugs",
  "jql": "type = Bug and resolution is empty",
  "name": "All Open Bugs"
}
```

## Original description

Updates a filter. Use this operation to update a filter's name, description, JQL, or sharing.

**[Permissions](#permissions) required:** Permission to access Jira, however the user must own the filter.
