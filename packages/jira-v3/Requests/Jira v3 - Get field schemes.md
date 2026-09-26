---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/config/fieldschemes"
category: "Field schemes"
writes_data: false
tool_note: "[[jira_get_field_schemes]]"
---
# Jira v3 - Get field schemes

**Get field schemes** — `GET /rest/api/3/config/fieldschemes`

- Run by the tool [[jira_get_field_schemes]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/config/fieldschemes?projectId={{param:projectId}}&query={{param:query}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectId` (query, string, optional) — (optional) List of project IDs to filter schemes by. If not provided, schemes from all projects are returned.
- `query` (query, string, optional) — (optional) Text filter for scheme name or description matching (case-insensitive). If not provided, no text filtering is applied.
- `startAt` (query, string, optional) — Zero-based index of the first item to return (default: 0)
- `maxResults` (query, string, optional) — Maximum number of items to return per page (default: 50, max: 100)

## Original description

REST endpoint for retrieving a paginated list of field association schemes with optional filtering.

This endpoint allows clients to fetch field association schemes with optional filtering by project IDs and text queries. The response includes scheme details with navigation links and filter metadata when applicable.

Filtering Behavior:

 *  When projectId or query parameters are provided, the response includes matchedFilters metadata showing which filters were applied.
 *  When no filters are applied, matchedFilters is omitted from individual scheme objects

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
