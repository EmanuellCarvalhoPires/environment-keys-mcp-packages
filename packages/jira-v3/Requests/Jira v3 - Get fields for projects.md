---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/projects/fields"
category: "Issue fields"
writes_data: false
tool_note: "[[jira_get_fields_for_projects]]"
---
# Jira v3 - Get fields for projects

**Get fields for projects** — `GET /rest/api/3/projects/fields`

- Run by the tool [[jira_get_fields_for_projects]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/projects/fields?startAt={{param:startAt}}&maxResults={{param:maxResults}}&projectId={{param:projectId}}&workTypeId={{param:workTypeId}}&fieldId={{param:fieldId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `projectId` (query, string, required) — The IDs of projects to return fields for.
- `workTypeId` (query, string, required) — The IDs of work types (issue types) to return fields for.
- `fieldId` (query, string, optional) — The IDs of fields to return. If not provided, all fields are returned.

## Original description

Returns a [paginated](#pagination) list of fields for the requested projects and work types.

Only fields that are available for the specified combination of projects and work types are returned. This endpoint allows filtering to specific fields if field IDs are provided.

**[Permissions](#permissions) required:** Permission to access Jira.
