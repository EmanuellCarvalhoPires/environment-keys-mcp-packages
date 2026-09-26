---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/config/fieldschemes/{id}/projects"
category: "Field schemes"
writes_data: false
tool_note: "[[jira_search_field_scheme_projects]]"
---
# Jira v3 - Search field scheme projects

**Search field scheme projects** — `GET /rest/api/3/config/fieldschemes/{id}/projects`

- Run by the tool [[jira_search_field_scheme_projects]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/config/fieldschemes/{{param:id}}/projects?startAt={{param:startAt}}&maxResults={{param:maxResults}}&projectId={{param:projectId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The scheme id to search for associated projects
- `startAt` (query, string, optional) — The starting index of the returned projects. Base index: 0.
- `maxResults` (query, string, optional) — The maximum number of projects to return per page, maximum allowed value is 100.
- `projectId` (query, string, optional) — The project Ids to filter by, if empty then all projects belonging to a field association scheme will be returned

## Original description

REST Endpoint for searching for projects belonging to a given field association scheme

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
