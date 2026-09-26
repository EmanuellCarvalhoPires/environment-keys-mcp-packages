---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/field/search/trashed"
category: "Issue fields"
writes_data: false
tool_note: "[[jira_get_fields_in_trash_paginated]]"
---
# Jira v3 - Get fields in trash paginated

**Get fields in trash paginated** — `GET /rest/api/3/field/search/trashed`

- Run by the tool [[jira_get_fields_in_trash_paginated]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/field/search/trashed?startAt={{param:startAt}}&maxResults={{param:maxResults}}&id={{param:id}}&query={{param:query}}&expand={{param:expand}}&orderBy={{param:orderBy}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `id` (query, string, optional) — Query parameter id.
- `query` (query, string, optional) — String used to perform a case-insensitive partial match with field names or descriptions.
- `expand` (query, string, optional) — Query parameter expand.
- `orderBy` (query, string, optional) — Order the results by a field: name sorts by the field name trashDate sorts by the date the field was moved to the trash plannedDeletionDate sorts by the planned deletion date

## Original description

Returns a [paginated](#pagination) list of fields in the trash. The list may be restricted to fields whose field name or description partially match a string.

Only custom fields can be queried, `type` must be set to `custom`.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
