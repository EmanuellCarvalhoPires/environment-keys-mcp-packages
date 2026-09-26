---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/agile/1.0/sprint/{sprintId}/issue"
category: "Sprint"
writes_data: false
tool_note: "[[jsw_get_issues_for_sprint]]"
---
# JSW - Get issues for sprint

**Get issues for sprint** — `GET /rest/agile/1.0/sprint/{sprintId}/issue`

- Run by the tool [[jsw_get_issues_for_sprint]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/sprint/{{param:sprintId}}/issue?startAt={{param:startAt}}&maxResults={{param:maxResults}}&jql={{param:jql}}&validateQuery={{param:validateQuery}}&fields={{param:fields}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `sprintId` (path, string, required) — The ID of the sprint that contains the requested issues.
- `startAt` (query, string, optional) — The starting index of the returned issues. Base index: 0. See the 'Pagination' section at the top of this page for more details.
- `maxResults` (query, string, optional) — The maximum number of issues to return per page. See the 'Pagination' section at the top of this page for more details.
- `jql` (query, string, optional) — Filters results using a JQL query. If you define an order in your JQL query, it will override the default order of the returned issues.
- `validateQuery` (query, string, optional) — Specifies whether to validate the JQL query or not. Default: true.
- `fields` (query, string, optional) — The list of fields to return for each issue. By default, all navigable and Agile fields are returned.
- `expand` (query, string, optional) — A comma-separated list of the parameters to expand.

## Original description

Returns all issues in a sprint, for a given sprint ID. This only includes issues that the user has permission to view. By default, the returned issues are ordered by rank.
