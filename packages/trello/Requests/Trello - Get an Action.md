---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/actions
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/actions/{id}"
category: "Actions"
writes_data: false
---
# Trello - Get an Action

**Get an Action** — `GET /actions/{id}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get an Action"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/actions/{{param:id}}?display={{param:display}}&entities={{param:entities}}&fields={{param:fields}}&member={{param:member}}&member_fields={{param:member_fields}}&memberCreator={{param:memberCreator}}&memberCreator_fields={{param:memberCreator_fields}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `display` (query, string, optional) — Query parameter display.
- `entities` (query, string, optional) — Query parameter entities.
- `fields` (query, string, optional) — all or a comma-separated list of action fields
- `member` (query, string, optional) — Query parameter member.
- `member_fields` (query, string, optional) — all or a comma-separated list of member fields
- `memberCreator` (query, string, optional) — Whether to include the member object for the creator of the action
- `memberCreator_fields` (query, string, optional) — all or a comma-separated list of member fields

## Original description

Get an Action

*Note: An action can live on a board or a workspace, so accessing it needs `read:board:trello` or `read:organization:trello`.*
