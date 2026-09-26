---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issuesecurityschemes/project"
category: "Issue security schemes"
writes_data: false
tool_note: "[[jira_get_projects_using_issue_security_schemes]]"
---
# Jira v3 - Get projects using issue security schemes

**Get projects using issue security schemes** — `GET /rest/api/3/issuesecurityschemes/project`

- Run by the tool [[jira_get_projects_using_issue_security_schemes]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issuesecurityschemes/project?startAt={{param:startAt}}&maxResults={{param:maxResults}}&issueSecuritySchemeId={{param:issueSecuritySchemeId}}&projectId={{param:projectId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `issueSecuritySchemeId` (query, string, optional) — The list of security scheme IDs to be filtered out.
- `projectId` (query, string, optional) — The list of project IDs to be filtered out.

## Original description

Returns a [paginated](#pagination) mapping of projects that are using security schemes. You can provide either one or multiple security scheme IDs or project IDs to filter by. If you don't provide any, this will return a list of all mappings. Only issue security schemes in the context of classic projects are supported. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
