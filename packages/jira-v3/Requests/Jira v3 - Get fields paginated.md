---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/field/search"
category: "Issue fields"
writes_data: false
tool_note: "[[jira_get_fields_paginated]]"
---
# Jira v3 - Get fields paginated

**Get fields paginated** — `GET /rest/api/3/field/search`

- Run by the tool [[jira_get_fields_paginated]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/field/search?startAt={{param:startAt}}&maxResults={{param:maxResults}}&type={{param:type}}&id={{param:id}}&query={{param:query}}&orderBy={{param:orderBy}}&expand={{param:expand}}&projectIds={{param:projectIds}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `type` (query, string, optional) — The type of fields to search.
- `id` (query, string, optional) — The IDs of the custom fields to return or, where query is specified, filter.
- `query` (query, string, optional) — String used to perform a case-insensitive partial match with field names or descriptions.
- `orderBy` (query, string, optional) — Order the results by: contextsCount sorts by the number of contexts related to a field lastUsed sorts by the date when the value of the field last changed name sorts by the field name screensCount sor…
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list.
- `projectIds` (query, string, optional) — The IDs of the projects to filter the fields by. Fields belonging to project Ids that the user does not have access to will not be returned

## Original description

Returns a [paginated](#pagination) list of fields for Classic Jira projects. The list can include:

 *  all fields
 *  specific fields, by defining `id`
 *  fields that contain a string in the field name or description, by defining `query`
 *  specific fields that contain a string in the field name or description, by defining `id` and `query`

Use `type` must be set to `custom` to show custom fields only.

**[Permissions](#permissions) required:** Permission to access Jira.
