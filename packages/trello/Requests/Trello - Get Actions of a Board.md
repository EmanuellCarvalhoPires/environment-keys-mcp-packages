---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/boards/{boardId}/actions"
category: "Boards"
writes_data: false
---
# Trello - Get Actions of a Board

**Get Actions of a Board** — `GET /boards/{boardId}/actions`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Actions of a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/boards/{{param:boardId}}/actions?fields={{param:fields}}&filter={{param:filter}}&format={{param:format}}&idModels={{param:idModels}}&limit={{param:limit}}&member={{param:member}}&member_fields={{param:member_fields}}&memberCreator={{param:memberCreator}}&memberCreator_fields={{param:memberCreator_fields}}&page={{param:page}}&reactions={{param:reactions}}&before={{param:before}}&since={{param:since}}
Authorization: {{service.auth_token}}
```

## Parameters

- `boardId` (path, string, required) — Value of boardId in the path.
- `fields` (query, string, optional) — The fields to be returned for the Actions. See Action fields here.
- `filter` (query, string, optional) — A comma-separated list of action types.
- `format` (query, string, optional) — The format of the returned Actions. Either list or count.
- `idModels` (query, string, optional) — A comma-separated list of idModels. Only actions related to these models will be returned.
- `limit` (query, string, optional) — The limit of the number of responses, between 0 and 1000.
- `member` (query, string, optional) — Whether to return the member object for each action.
- `member_fields` (query, string, optional) — The fields of the member to return.
- `memberCreator` (query, string, optional) — Whether to return the memberCreator object for each action.
- `memberCreator_fields` (query, string, optional) — The fields of the member creator to return
- `page` (query, string, optional) — The page of results for actions.
- `reactions` (query, string, optional) — Whether to show reactions on comments or not.
- `before` (query, string, optional) — A date string in the form of YYYY-MM-DDThh:mm:ssZ or a mongo object ID. Only objects created before this date will be returned.
- `since` (query, string, optional) — A date string in the form of YYYY-MM-DDThh:mm:ssZ or a mongo object ID. Only objects created since this date will be returned.

## Original description

Get all of the actions of a Board. See [Nested Resources](/cloud/trello/guides/rest-api/nested-resources/) for more information.
