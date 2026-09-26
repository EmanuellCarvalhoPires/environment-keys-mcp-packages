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
path: "/rest/software/1.0/board/{boardId}/backlog"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_issues_for_backlog_enhanced]]"
---
# JSW - Get issues for backlog (enhanced)

**Get issues for backlog (enhanced)** — `GET /rest/software/1.0/board/{boardId}/backlog`

- Run by the tool [[jsw_get_issues_for_backlog_enhanced]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/software/1.0/board/{{param:boardId}}/backlog?nextPageToken={{param:nextPageToken}}&maxResults={{param:maxResults}}&reconcileIssues={{param:reconcileIssues}}&jql={{param:jql}}&validateQuery={{param:validateQuery}}&fields={{param:fields}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `boardId` (path, string, required) — The ID of the board that has the backlog containing the requested issues.
- `nextPageToken` (query, string, optional) — The token for a page to fetch that is not the first page. The first page has a nextPageToken of null. Use the nextPageToken to fetch the next page of issues.
- `maxResults` (query, string, optional) — The maximum number of items to return per page. To manage page size, the API may return fewer items per page where there is a large number of fields or properties returned. It returns max 5000 issues.
- `reconcileIssues` (query, string, optional) — Strong consistency issue IDs to be reconciled with search results. Accepts max 50 IDs. This list of IDs should be consistent with each paginated request across different pages.
- `jql` (query, string, optional) — Filters results using a JQL query. If you define an order in your JQL query, it will override the default order of the returned issues.
- `validateQuery` (query, string, optional) — Specifies whether to validate the JQL query or not. Default: true.
- `fields` (query, string, optional) — The list of fields to return for each issue. By default, all navigable and Software project fields are returned.
- `expand` (query, string, optional) — A comma-separated list of the parameters to expand.

## Original description

Returns all issues from the board's backlog, for the given board ID. Result pagination is token based, using `nextPageToken` and `maxResults`. This only includes issues that the user has permission to view. Note, if the user does not have permission to view the board, no issues will be returned at all. The backlog contains incomplete issues that are not assigned to any future or active sprint. Issues returned from this resource include Software project fields, like sprint, closedSprints, flagged, and epic. By default, the returned issues are ordered by rank.
