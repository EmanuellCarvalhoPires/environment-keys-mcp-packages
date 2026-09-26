---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-screen-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issuetypescreenscheme/project"
category: "Issue type screen schemes"
writes_data: false
tool_note: "[[jira_get_issue_type_screen_schemes_for_projects]]"
---
# Jira v3 - Get issue type screen schemes for projects

**Get issue type screen schemes for projects** — `GET /rest/api/3/issuetypescreenscheme/project`

- Run by the tool [[jira_get_issue_type_screen_schemes_for_projects]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issuetypescreenscheme/project?startAt={{param:startAt}}&maxResults={{param:maxResults}}&projectId={{param:projectId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `projectId` (query, string, required) — The list of project IDs. To include multiple projects, separate IDs with ampersand: projectId=10000&projectId=10001.

## Original description

Returns a [paginated](#pagination) list of issue type screen schemes and, for each issue type screen scheme, a list of the projects that use it.

Only issue type screen schemes used in classic projects are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
