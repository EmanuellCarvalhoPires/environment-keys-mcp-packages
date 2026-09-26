---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-schemes
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issuesecurityschemes/search"
category: "Issue security schemes"
writes_data: false
tool_note: "[[jira_search_issue_security_schemes]]"
---
# Jira v3 - Search issue security schemes

**Search issue security schemes** — `GET /rest/api/3/issuesecurityschemes/search`

- Run by the tool [[jira_search_issue_security_schemes]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issuesecurityschemes/search?startAt={{param:startAt}}&maxResults={{param:maxResults}}&id={{param:id}}&projectId={{param:projectId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `id` (query, string, optional) — The list of issue security scheme IDs. To include multiple issue security scheme IDs, separate IDs with an ampersand: id=10000&id=10001.
- `projectId` (query, string, optional) — The list of project IDs. To include multiple project IDs, separate IDs with an ampersand: projectId=10000&projectId=10001.

## Original description

Returns a [paginated](#pagination) list of issue security schemes.  
If you specify the project ID parameter, the result will contain issue security schemes and related project IDs you filter by. Use \{@link IssueSecuritySchemeResource\#searchProjectsUsingSecuritySchemes(String, String, Set, Set)\} to obtain all projects related to scheme.

Only issue security schemes in the context of classic projects are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
