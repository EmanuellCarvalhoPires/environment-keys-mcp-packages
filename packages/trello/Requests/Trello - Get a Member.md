---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/members/{id}"
category: "Members"
writes_data: false
---
# Trello - Get a Member

**Get a Member** — `GET /members/{id}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Member"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}?actions={{param:actions}}&boards={{param:boards}}&boardBackgrounds={{param:boardBackgrounds}}&boardsInvited={{param:boardsInvited}}&boardsInvited_fields={{param:boardsInvited_fields}}&boardStars={{param:boardStars}}&cards={{param:cards}}&customBoardBackgrounds={{param:customBoardBackgrounds}}&customEmoji={{param:customEmoji}}&customStickers={{param:customStickers}}&fields={{param:fields}}&notifications={{param:notifications}}&organizations={{param:organizations}}&organization_fields={{param:organization_fields}}&organization_paid_account={{param:organization_paid_account}}&organizationsInvited={{param:organizationsInvited}}&organizationsInvited_fields={{param:organizationsInvited_fields}}&paid_account={{param:paid_account}}&savedSearches={{param:savedSearches}}&tokens={{param:tokens}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or username of the member
- `actions` (query, string, optional) — See the Actions Nested Resource
- `boards` (query, string, optional) — See the Boards Nested Resource
- `boardBackgrounds` (query, string, optional) — One of: all, custom, default, none, premium
- `boardsInvited` (query, string, optional) — all or a comma-separated list of: closed, members, open, organization, pinned, public, starred, unpinned
- `boardsInvited_fields` (query, string, optional) — all or a comma-separated list of board fields
- `boardStars` (query, string, optional) — Whether to return the boardStars or not
- `cards` (query, string, optional) — See the Cards Nested Resource for additional options
- `customBoardBackgrounds` (query, string, optional) — all or none
- `customEmoji` (query, string, optional) — all or none
- `customStickers` (query, string, optional) — all or none
- `fields` (query, string, optional) — all or a comma-separated list of member fields
- `notifications` (query, string, optional) — See the Notifications Nested Resource
- `organizations` (query, string, optional) — One of: all, members, none, public
- `organization_fields` (query, string, optional) — all or a comma-separated list of organization fields
- `organization_paid_account` (query, string, optional) — Whether or not to include paid account information in the returned workspace object
- `organizationsInvited` (query, string, optional) — One of: all, members, none, public
- `organizationsInvited_fields` (query, string, optional) — all or a comma-separated list of organization fields
- `paid_account` (query, string, optional) — Whether or not to include paid account information in the returned member object
- `savedSearches` (query, string, optional) — Query parameter savedSearches.
- `tokens` (query, string, optional) — all or none

## Original description

Get a member
