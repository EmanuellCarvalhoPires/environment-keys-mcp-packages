---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/search
  - api/operation/search
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/search"
category: "Search"
writes_data: false
---
# Trello - Search Trello

**Search Trello** — `GET /search`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Search Trello"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/search?query={{param:query}}&idBoards={{param:idBoards}}&idOrganizations={{param:idOrganizations}}&idCards={{param:idCards}}&modelTypes={{param:modelTypes}}&board_fields={{param:board_fields}}&boards_limit={{param:boards_limit}}&board_organization={{param:board_organization}}&card_fields={{param:card_fields}}&cards_limit={{param:cards_limit}}&cards_page={{param:cards_page}}&card_board={{param:card_board}}&card_list={{param:card_list}}&card_members={{param:card_members}}&card_stickers={{param:card_stickers}}&card_attachments={{param:card_attachments}}&organization_fields={{param:organization_fields}}&organizations_limit={{param:organizations_limit}}&member_fields={{param:member_fields}}&members_limit={{param:members_limit}}&partial={{param:partial}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `query` (query, string, required) — The search query with a length of 1 to 16384 characters
- `idBoards` (query, string, optional) — mine or a comma-separated list of Board IDs
- `idOrganizations` (query, string, optional) — A comma-separated list of Organization IDs
- `idCards` (query, string, optional) — A comma-separated list of Card IDs
- `modelTypes` (query, string, optional) — What type or types of Trello objects you want to search. all or a comma-separated list of: actions, boards, cards, members, organizations
- `board_fields` (query, string, optional) — all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, short…
- `boards_limit` (query, string, optional) — The maximum number of boards returned. Maximum: 1000
- `board_organization` (query, string, optional) — Whether to include the parent organization with board results
- `card_fields` (query, string, optional) — all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort…
- `cards_limit` (query, string, optional) — The maximum number of cards to return. Maximum: 1000
- `cards_page` (query, string, optional) — The page of results for cards. Maximum: 100
- `card_board` (query, string, optional) — Whether to include the parent board with card results
- `card_list` (query, string, optional) — Whether to include the parent list with card results
- `card_members` (query, string, optional) — Whether to include member objects with card results
- `card_stickers` (query, string, optional) — Whether to include sticker objects with card results
- `card_attachments` (query, string, optional) — Whether to include attachment objects with card results. A boolean value (true or false) or cover for only card cover attachments.
- `organization_fields` (query, string, optional) — all or a comma-separated list of billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url, website
- `organizations_limit` (query, string, optional) — The maximum number of Workspaces to return. Maximum 1000
- `member_fields` (query, string, optional) — all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url, username
- `members_limit` (query, string, optional) — The maximum number of members to return. Maximum 1000
- `partial` (query, string, optional) — By default, Trello searches for each word in your query against exactly matching words within Member content.

## Original description

Find what you're looking for in Trello
