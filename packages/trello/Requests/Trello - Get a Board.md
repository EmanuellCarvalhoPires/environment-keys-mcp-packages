---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/boards/{id}"
category: "Boards"
writes_data: false
---
# Trello - Get a Board

**Get a Board** — `GET /boards/{id}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/boards/{{param:id}}?actions={{param:actions}}&boardStars={{param:boardStars}}&cards={{param:cards}}&card_pluginData={{param:card_pluginData}}&checklists={{param:checklists}}&customFields={{param:customFields}}&fields={{param:fields}}&labels={{param:labels}}&lists={{param:lists}}&members={{param:members}}&memberships={{param:memberships}}&pluginData={{param:pluginData}}&organization={{param:organization}}&organization_pluginData={{param:organization_pluginData}}&myPrefs={{param:myPrefs}}&tags={{param:tags}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `actions` (query, string, optional) — This is a nested resource. Read more about actions as nested resources here.
- `boardStars` (query, string, optional) — Valid values are one of: mine or none.
- `cards` (query, string, optional) — This is a nested resource. Read more about cards as nested resources here.
- `card_pluginData` (query, string, optional) — Use with the cards param to include card pluginData with the response
- `checklists` (query, string, optional) — This is a nested resource. Read more about checklists as nested resources here.
- `customFields` (query, string, optional) — This is a nested resource. Read more about custom fields as nested resources here.
- `fields` (query, string, optional) — The fields of the board to be included in the response. Valid values: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idMemberCreator, idOrganization, invitat…
- `labels` (query, string, optional) — This is a nested resource. Read more about labels as nested resources here.
- `lists` (query, string, optional) — This is a nested resource. Read more about lists as nested resources here.
- `members` (query, string, optional) — This is a nested resource. Read more about members as nested resources here.
- `memberships` (query, string, optional) — This is a nested resource. Read more about memberships as nested resources here.
- `pluginData` (query, string, optional) — Determines whether the pluginData for this board should be returned. Valid values: true or false.
- `organization` (query, string, optional) — This is a nested resource. Read more about organizations as nested resources here.
- `organization_pluginData` (query, string, optional) — Use with the organization param to include organization pluginData with the response
- `myPrefs` (query, string, optional) — Query parameter myPrefs.
- `tags` (query, string, optional) — Also known as collections, tags, refer to the collection(s) that a Board belongs to.

## Original description

Request a single board.
