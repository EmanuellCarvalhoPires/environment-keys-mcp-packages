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
path: "/rest/agile/1.0/board/{boardId}/configuration"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_configuration]]"
---
# JSW - Get configuration

**Get configuration** — `GET /rest/agile/1.0/board/{boardId}/configuration`

- Run by the tool [[jsw_get_configuration]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/board/{{param:boardId}}/configuration
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `boardId` (path, string, required) — The ID of the board for which configuration is requested.

## Original description

Get the board configuration. The response contains the following fields:

 *  `id` \- ID of the board.
 *  `name` \- Name of the board.
 *  `filter` \- Reference to the filter used by the given board.
 *  `location` \- Reference to the container that the board is located in. Includes the container type (Valid values: project, user).
 *  `subQuery` (Kanban only) - JQL subquery used by the given board.
 *  `columnConfig` \- The column configuration lists the columns for the board, in the order defined in the column configuration. For each column, it shows the issue status mapping as well as the constraint type (Valid values: none, issueCount, issueCountExclSubs) for the min/max number of issues. Note, the last column with statuses mapped to it is treated as the "Done" column, which means that issues in that column will be marked as already completed.
 *  `estimation` (Scrum only) - Contains information about type of estimation used for the board. Valid values: none, issueCount, field. If the estimation type is "field", the ID and display name of the field used for estimation is also returned. Note, estimates for an issue can be updated by a PUT /rest/api/3/issue/\{issueIdOrKey\} request, however the fields must be on the screen. "timeoriginalestimate" field will never be on the screen, so in order to update it "originalEstimate" in "timetracking" field should be updated.
 *  `ranking` \- Contains information about custom field used for ranking in the given board.
