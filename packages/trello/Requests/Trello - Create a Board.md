---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/boards/"
category: "Boards"
writes_data: true
---
# Trello - Create a Board

**Create a Board** — `POST /boards/`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/boards/?name={{param:name}}&defaultLabels={{param:defaultLabels}}&defaultLists={{param:defaultLists}}&desc={{param:desc}}&idOrganization={{param:idOrganization}}&idBoardSource={{param:idBoardSource}}&keepFromSource={{param:keepFromSource}}&powerUps={{param:powerUps}}&prefs_permissionLevel={{param:prefs_permissionLevel}}&prefs_voting={{param:prefs_voting}}&prefs_comments={{param:prefs_comments}}&prefs_invitations={{param:prefs_invitations}}&prefs_selfJoin={{param:prefs_selfJoin}}&prefs_cardCovers={{param:prefs_cardCovers}}&prefs_background={{param:prefs_background}}&prefs_cardAging={{param:prefs_cardAging}}
Authorization: {{service.auth_token}}
```

## Parameters

- `name` (query, string, required) — The new name for the board. 1 to 16384 characters long.
- `defaultLabels` (query, string, optional) — Determines whether to use the default set of labels.
- `defaultLists` (query, string, optional) — Determines whether to add the default set of lists to a board (To Do, Doing, Done). It is ignored if idBoardSource is provided.
- `desc` (query, string, optional) — A new description for the board, 0 to 16384 characters long
- `idOrganization` (query, string, optional) — The id or name of the Workspace the board should belong to.
- `idBoardSource` (query, string, optional) — The id of a board to copy into the new board.
- `keepFromSource` (query, string, optional) — To keep cards from the original board pass in the value cards
- `powerUps` (query, string, optional) — The Power-Ups that should be enabled on the new board. One of: all, calendar, cardAging, recap, voting.
- `prefs_permissionLevel` (query, string, optional) — The permissions level of the board. One of: org, private, public.
- `prefs_voting` (query, string, optional) — Who can vote on this board. One of disabled, members, observers, org, public.
- `prefs_comments` (query, string, optional) — Who can comment on cards on this board. One of: disabled, members, observers, org, public.
- `prefs_invitations` (query, string, optional) — Determines what types of members can invite users to join. One of: admins, members.
- `prefs_selfJoin` (query, string, optional) — Determines whether users can join the boards themselves or whether they have to be invited.
- `prefs_cardCovers` (query, string, optional) — Determines whether card covers are enabled.
- `prefs_background` (query, string, optional) — The id of a custom background or one of: blue, orange, green, red, purple, pink, lime, sky, grey.
- `prefs_cardAging` (query, string, optional) — Determines the type of card aging that should take place on the board if card aging is enabled. One of: pirate, regular.

## Original description

Create a new board.
