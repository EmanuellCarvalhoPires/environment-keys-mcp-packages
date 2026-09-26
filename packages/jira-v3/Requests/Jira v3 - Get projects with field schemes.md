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
path: "/rest/api/3/config/fieldschemes/projects"
category: "Field schemes"
writes_data: false
tool_note: "[[jira_get_projects_with_field_schemes]]"
---
# Jira v3 - Get projects with field schemes

**Get projects with field schemes** — `GET /rest/api/3/config/fieldschemes/projects`

- Run by the tool [[jira_get_projects_with_field_schemes]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/config/fieldschemes/projects?startAt={{param:startAt}}&maxResults={{param:maxResults}}&projectId={{param:projectId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The starting index of the returned projects. Base index: 0.
- `maxResults` (query, string, optional) — The maximum number of projects to return per page, maximum allowed value is 100.
- `projectId` (query, string, required) — List of project ids to filter the results by.

## Original description

Get projects with field association schemes. This will be a temporary API but useful when transitioning from the legacy field configuration APIs to the new ones.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
