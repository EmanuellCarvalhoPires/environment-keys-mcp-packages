---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/epic
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/agile/1.0/epic/none/issue"
category: "Epic"
writes_data: false
tool_note: "[[jsw_get_issues_without_epic]]"
---
# JSW - Get issues without epic

**Get issues without epic** — `GET /rest/agile/1.0/epic/none/issue`

- Run by the tool [[jsw_get_issues_without_epic]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/epic/none/issue?startAt={{param:startAt}}&maxResults={{param:maxResults}}&jql={{param:jql}}&validateQuery={{param:validateQuery}}&fields={{param:fields}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The starting index of the returned issues. Base index: 0. See the 'Pagination' section at the top of this page for more details.
- `maxResults` (query, string, optional) — The maximum number of issues to return per page. See the 'Pagination' section at the top of this page for more details.
- `jql` (query, string, optional) — Filters results using a JQL query. If you define an order in your JQL query, it will override the default order of the returned issues.
- `validateQuery` (query, string, optional) — Specifies whether to validate the JQL query or not. Default: true.
- `fields` (query, string, optional) — The list of fields to return for each issue. By default, all navigable and Agile fields are returned.
- `expand` (query, string, optional) — A comma-separated list of the parameters to expand.

## Original description

Returns all issues that do not belong to any epic. This only includes issues that the user has permission to view. Issues returned from this resource include Agile fields, like sprint, closedSprints, flagged, and epic. By default, the returned issues are ordered by rank. **Note:** If you are querying a next-gen project, do not use this operation. Instead, search for issues that don't belong to an epic by using the [Search for issues using JQL](https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-rest-api-2-search-get) operation in the Jira platform REST API. Build your JQL query using the `parent is empty` clause. For more information on the `parent` JQL field, see [Advanced searching](https://confluence.atlassian.com/x/dAiiLQ#Advancedsearching-fieldsreference-Parent).
