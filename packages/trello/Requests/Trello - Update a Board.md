---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/boards/{id}"
category: "Boards"
writes_data: true
---
# Trello - Update a Board

**Update a Board** — `PUT /boards/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/boards/{{param:id}}?name={{param:name}}&desc={{param:desc}}&closed={{param:closed}}&subscribed={{param:subscribed}}&idOrganization={{param:idOrganization}}&prefs/permissionLevel={{param:prefs_permissionLevel}}&prefs/selfJoin={{param:prefs_selfJoin}}&prefs/cardCovers={{param:prefs_cardCovers}}&prefs/hideVotes={{param:prefs_hideVotes}}&prefs/invitations={{param:prefs_invitations}}&prefs/voting={{param:prefs_voting}}&prefs/comments={{param:prefs_comments}}&prefs/background={{param:prefs_background}}&prefs/cardAging={{param:prefs_cardAging}}&prefs/calendarFeedEnabled={{param:prefs_calendarFeedEnabled}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `name` (query, string, optional) — The new name for the board. 1 to 16384 characters long.
- `desc` (query, string, optional) — A new description for the board, 0 to 16384 characters long
- `closed` (query, string, optional) — Whether the board is closed
- `subscribed` (query, string, optional) — Whether the acting user is subscribed to the board
- `idOrganization` (query, string, optional) — The id of the Workspace the board should be moved to
- `prefs_permissionLevel` (query, string, optional) — One of: org, private, public
- `prefs_selfJoin` (query, string, optional) — Whether Workspace members can join the board themselves
- `prefs_cardCovers` (query, string, optional) — Whether card covers should be displayed on this board
- `prefs_hideVotes` (query, string, optional) — Determines whether the Voting Power-Up should hide who voted on cards or not.
- `prefs_invitations` (query, string, optional) — Who can invite people to this board. One of: admins, members
- `prefs_voting` (query, string, optional) — Who can vote on this board. One of disabled, members, observers, org, public
- `prefs_comments` (query, string, optional) — Who can comment on cards on this board. One of: disabled, members, observers, org, public
- `prefs_background` (query, string, optional) — The id of a custom background or one of: blue, orange, green, red, purple, pink, lime, sky, grey
- `prefs_cardAging` (query, string, optional) — One of: pirate, regular
- `prefs_calendarFeedEnabled` (query, string, optional) — Determines whether the calendar feed is enabled or not.

## Original description

Update an existing board by id
