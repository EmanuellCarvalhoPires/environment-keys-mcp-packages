---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes/{issueTypeId}"
category: "Issues"
writes_data: false
tool_note: "[[jira_get_create_field_metadata_for_a_project_and_issue_type_id]]"
---
# Jira v3 - Get create field metadata for a project and issue type id

**Get create field metadata for a project and issue type id** — `GET /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes/{issueTypeId}`

- Run by the tool [[jira_get_create_field_metadata_for_a_project_and_issue_type_id]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issue/createmeta/{{param:projectIdOrKey}}/issuetypes/{{param:issueTypeId}}?startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The ID or key of the project.
- `issueTypeId` (path, string, required) — The issuetype ID.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.

## Original description

Returns a page of field metadata for a specified project and issuetype id. Use the information to populate the requests in [ Create issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Create issues* [project permission](https://confluence.atlassian.com/x/yodKLg) in the requested projects.
