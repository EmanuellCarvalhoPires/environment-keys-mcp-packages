---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/cards
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/cards/{id}/actions"
category: "Cards"
writes_data: false
---
# Trello - Get Actions on a Card

**Get Actions on a Card** — `GET /cards/{id}/actions`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Actions on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/cards/{{param:id}}/actions?filter={{param:filter}}&page={{param:page}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the Card
- `filter` (query, string, optional) — A comma-separated list of action types.
- `page` (query, string, optional) — The page of results for actions. Each page of results has 50 actions.

## Original description

List the Actions on a Card. See [Nested Resources](/cloud/trello/guides/rest-api/nested-resources/) for more information.
