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
path: "/rest/agile/1.0/board"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_all_boards]]"
---
# JSW - Get all boards

**Get all boards** — `GET /rest/agile/1.0/board`

- Run by the tool [[jsw_get_all_boards]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/board?startAt={{param:startAt}}&maxResults={{param:maxResults}}&type={{param:type}}&name={{param:name}}&projectKeyOrId={{param:projectKeyOrId}}&accountIdLocation={{param:accountIdLocation}}&projectLocation={{param:projectLocation}}&includePrivate={{param:includePrivate}}&negateLocationFiltering={{param:negateLocationFiltering}}&orderBy={{param:orderBy}}&expand={{param:expand}}&projectTypeLocation={{param:projectTypeLocation}}&filterId={{param:filterId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The starting index of the returned boards. Base index: 0. See the 'Pagination' section at the top of this page for more details.
- `maxResults` (query, string, optional) — The maximum number of boards to return per page. See the 'Pagination' section at the top of this page for more details.
- `type` (query, string, optional) — Filters results to boards of the specified types. Valid values: scrum, kanban, simple.
- `name` (query, string, optional) — Filters results to boards that match or partially match the specified name.
- `projectKeyOrId` (query, string, optional) — Filters results to boards that are relevant to a project. Relevance means that the jql filter defined in board contains a reference to a project.
- `accountIdLocation` (query, string, optional) — Query parameter accountIdLocation.
- `projectLocation` (query, string, optional) — Query parameter projectLocation.
- `includePrivate` (query, string, optional) — Appends private boards to the end of the list. The name and type fields are excluded for security reasons.
- `negateLocationFiltering` (query, string, optional) — If set to true, negate filters used for querying by location. By default false.
- `orderBy` (query, string, optional) — Ordering of the results by a given field. If not provided, values will not be sorted. Valid values: name.
- `expand` (query, string, optional) — List of fields to expand for each board. Valid values: admins, permissions.
- `projectTypeLocation` (query, string, optional) — Filters results to boards that are relevant to a project types. Support Jira Software, Jira Service Management. Valid values: software, service\desk. By default software.
- `filterId` (query, string, optional) — Filters results to boards that are relevant to a filter. Not supported for next-gen boards.

## Original description

Returns all boards. This only includes boards that the user has permission to view.

**Deprecation notice:** The required OAuth 2.0 scopes will be updated on February 15, 2024.

 *  `read:board-scope:jira-software`, `read:project:jira`
