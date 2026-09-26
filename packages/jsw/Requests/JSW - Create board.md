---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSW]]"
app: "JSW"
method: POST
path: "/rest/agile/1.0/board"
category: "Board"
writes_data: true
tool_note: "[[jsw_create_board]]"
---
# JSW - Create board

**Create board** — `POST /rest/agile/1.0/board`

- Run by the tool [[jsw_create_board]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/agile/1.0/board
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "filterId": 10040,
  "location": {
    "projectKeyOrId": "10000",
    "type": "project"
  },
  "name": "scrum board",
  "type": "scrum"
}
```

## Original description

Creates a new board. Board name, type and filter ID is required.

 *  `name` \- Must be less than 255 characters.
 *  `type` \- Valid values: scrum, kanban
 *  `filterId` \- ID of a filter that the user has permissions to view. Note, if the user does not have the 'Create shared objects' permission and tries to create a shared board, a private board will be created instead (remember that board sharing depends on the filter sharing).
 *  `location` \- The container that the board will be located in. `location` must include the `type` property (Valid values: project, user). If choosing 'project', then a project must be specified by a `projectKeyOrId` property in `location`. If choosing 'user', the current user is chosen by default. The `projectKeyOrId` property should not be provided.

Note:

 *  If you want to create a new project with an associated board, use the [Jira platform REST API](https://docs.atlassian.com/jira/REST/latest). For more information, see the [Create project](#api-rest-api-3-project-post) method. The `projectTypeKey` for software boards must be 'software' and the `projectTemplateKey` must be either `com.pyxis.greenhopper.jira:gh-kanban-template` or `com.pyxis.greenhopper.jira:gh-scrum-template`.
 *  You can create a filter using the [Jira REST API](https://docs.atlassian.com/jira/REST/latest). For more information, see the [Create filter](#api-rest-api-3-filter-post) method.
 *  If you do not ORDER BY the Rank field for the filter of your board, you will not be able to reorder issues on the board.
