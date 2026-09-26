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
path: "/rest/software/1.0/board/{boardId}/backlog/approximate-count"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_approximate_issue_count_for_backlog]]"
---
# JSW - Get approximate issue count for backlog

**Get approximate issue count for backlog** — `GET /rest/software/1.0/board/{boardId}/backlog/approximate-count`

- Run by the tool [[jsw_get_approximate_issue_count_for_backlog]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/software/1.0/board/{{param:boardId}}/backlog/approximate-count?jql={{param:jql}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `boardId` (path, string, required) — The ID of the board that has the backlog containing the requested issues.
- `jql` (query, string, optional) — Filters results using a JQL query. Note that username and userkey can't be used as search terms for this parameter due to privacy reasons. Use accountId instead.

## Original description

Returns the approximate count of all issues from the board's backlog, for the given board ID. This is equivalent to counting the issues on all pages returned by [Get issues for backlog enhanced](https://developer.atlassian.com/cloud/jira/software/rest/api-group-board/#api-rest-software-1-0-board-boardid-backlog-get). Recent updates might not be immediately visible in the returned output. This only includes issues that the user has permission to view.
