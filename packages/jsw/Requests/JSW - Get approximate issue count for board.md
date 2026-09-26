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
path: "/rest/software/1.0/board/{boardId}/issue/approximate-count"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_approximate_issue_count_for_board]]"
---
# JSW - Get approximate issue count for board

**Get approximate issue count for board** — `GET /rest/software/1.0/board/{boardId}/issue/approximate-count`

- Run by the tool [[jsw_get_approximate_issue_count_for_board]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/software/1.0/board/{{param:boardId}}/issue/approximate-count?jql={{param:jql}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `boardId` (path, string, required) — The ID of the board that contains the requested issues.
- `jql` (query, string, optional) — Filters results using a JQL query. Note that username and userkey can't be used as search terms for this parameter due to privacy reasons. Use accountId instead.

## Original description

Returns the approximate count of all issues from a board, for a given board ID. This is equivalent to counting the issues on all pages returned by [Get issues for board enhanced](https://developer.atlassian.com/cloud/jira/software/rest/api-group-board/#api-rest-software-1-0-board-boardid-issue-get). Recent updates might not be immediately visible in the returned output. This only includes issues that the user has permission to view.
