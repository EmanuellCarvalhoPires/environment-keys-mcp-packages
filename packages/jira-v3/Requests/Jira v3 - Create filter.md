---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/filter"
category: "Filters"
writes_data: true
tool_note: "[[jira_create_filter]]"
---
# Jira v3 - Create filter

**Create filter** — `POST /rest/api/3/filter`

- Run by the tool [[jira_create_filter]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/filter?expand={{param:expand}}&overrideSharePermissions={{param:overrideSharePermissions}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `expand` (query, string, optional) — Use expand to include additional information about filter in the response. This parameter accepts a comma-separated list.
- `overrideSharePermissions` (query, string, optional) — EXPERIMENTAL: Whether share permissions are overridden to enable filters with any share permissions to be created. Available to users with Administer Jira global permission.
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

Creates a filter. The filter is shared according to the [default share scope](#api-rest-api-3-filter-post). The filter is not selected as a favorite.

**[Permissions](#permissions) required:** Permission to access Jira.
