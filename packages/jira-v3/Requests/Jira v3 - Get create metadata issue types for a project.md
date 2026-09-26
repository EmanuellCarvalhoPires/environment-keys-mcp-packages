---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes"
category: "Issues"
writes_data: false
tool_note: "[[jira_get_create_metadata_issue_types_for_a_project]]"
---
# Jira v3 - Get create metadata issue types for a project

**Get create metadata issue types for a project** — `GET /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes`

- Run by the tool [[jira_get_create_metadata_issue_types_for_a_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issue/createmeta/{{param:projectIdOrKey}}/issuetypes?startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The ID or key of the project.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.

## Original description

Returns a page of issue type metadata for a specified project. Use the information to populate the requests in [ Create issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Create issues* [project permission](https://confluence.atlassian.com/x/yodKLg) in the requested projects.
