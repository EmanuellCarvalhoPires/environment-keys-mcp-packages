---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/agile/1.0/board/{boardId}/epic/{epicId}/issue"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_board_issues_for_epic]]"
---
# JSW - Get board issues for epic

**Get board issues for epic** — `GET /rest/agile/1.0/board/{boardId}/epic/{epicId}/issue`

- Run by the tool [[jsw_get_board_issues_for_epic]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/board/{{param:boardId}}/epic/{{param:epicId}}/issue?startAt={{param:startAt}}&maxResults={{param:maxResults}}&jql={{param:jql}}&validateQuery={{param:validateQuery}}&fields={{param:fields}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `boardId` (path, string, required) — The ID of the board that contains the requested issues.
- `epicId` (path, string, required) — The ID of the epic that contains the requested issues.
- `startAt` (query, string, optional) — The starting index of the returned issues. Base index: 0. See the 'Pagination' section at the top of this page for more details.
- `maxResults` (query, string, optional) — The maximum number of issues to return per page. Default: 50. See the 'Pagination' section at the top of this page for more details.
- `jql` (query, string, optional) — Filters results using a JQL query. If you define an order in your JQL query, it will override the default order of the returned issues.
- `validateQuery` (query, string, optional) — Specifies whether to validate the JQL query or not. Default: true.
- `fields` (query, string, optional) — The list of fields to return for each issue. By default, all navigable and Agile fields are returned.
- `expand` (query, string, optional) — A comma-separated list of the parameters to expand.

## Original description

Returns all issues that belong to an epic on the board, for the given epic ID and the board ID. This only includes issues that the user has permission to view. Issues returned from this resource include Agile fields, like sprint, closedSprints, flagged, and epic. By default, the returned issues are ordered by rank.
