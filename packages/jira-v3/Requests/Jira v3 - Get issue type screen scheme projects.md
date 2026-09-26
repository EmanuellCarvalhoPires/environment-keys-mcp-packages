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
path: "/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/project"
category: "Issue type screen schemes"
writes_data: false
tool_note: "[[jira_get_issue_type_screen_scheme_projects]]"
---
# Jira v3 - Get issue type screen scheme projects

**Get issue type screen scheme projects** — `GET /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/project`

- Run by the tool [[jira_get_issue_type_screen_scheme_projects]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issuetypescreenscheme/{{param:issueTypeScreenSchemeId}}/project?startAt={{param:startAt}}&maxResults={{param:maxResults}}&query={{param:query}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueTypeScreenSchemeId` (path, string, required) — The ID of the issue type screen scheme.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `query` (query, string, optional) — Query parameter query.

## Original description

Returns a [paginated](#pagination) list of projects associated with an issue type screen scheme.

Only company-managed projects associated with an issue type screen scheme are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
