---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/cards
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/cards/{id}"
category: "Cards"
writes_data: false
---
# Trello - Get a Card

**Get a Card** — `GET /cards/{id}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/cards/{{param:id}}?fields={{param:fields}}&actions={{param:actions}}&attachments={{param:attachments}}&attachment_fields={{param:attachment_fields}}&members={{param:members}}&member_fields={{param:member_fields}}&membersVoted={{param:membersVoted}}&memberVoted_fields={{param:memberVoted_fields}}&checkItemStates={{param:checkItemStates}}&checklists={{param:checklists}}&checklist_fields={{param:checklist_fields}}&board={{param:board}}&board_fields={{param:board_fields}}&list={{param:list}}&pluginData={{param:pluginData}}&stickers={{param:stickers}}&sticker_fields={{param:sticker_fields}}&customFieldItems={{param:customFieldItems}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `fields` (query, string, optional) — all or a comma-separated list of fields. Defaults: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, start, idBoard, idChecklists, idLabels, idList, idMembers, idShort, idAttachm…
- `actions` (query, string, optional) — See the Actions Nested Resource
- `attachments` (query, string, optional) — true, false, or cover
- `attachment_fields` (query, string, optional) — all or a comma-separated list of attachment fields
- `members` (query, string, optional) — Whether to return member objects for members on the card
- `member_fields` (query, string, optional) — all or a comma-separated list of member fields. Defaults: avatarHash, fullName, initials, username
- `membersVoted` (query, string, optional) — Whether to return member objects for members who voted on the card
- `memberVoted_fields` (query, string, optional) — all or a comma-separated list of member fields. Defaults: avatarHash, fullName, initials, username
- `checkItemStates` (query, string, optional) — Query parameter checkItemStates.
- `checklists` (query, string, optional) — Whether to return the checklists on the card. all or none
- `checklist_fields` (query, string, optional) — all or a comma-separated list of idBoard,idCard,name,pos
- `board` (query, string, optional) — Whether to return the board object the card is on
- `board_fields` (query, string, optional) — all or a comma-separated list of board fields. Defaults: name, desc, descData, closed, idOrganization, pinned, url, prefs
- `list` (query, string, optional) — See the Lists Nested Resource
- `pluginData` (query, string, optional) — Whether to include pluginData on the card with the response
- `stickers` (query, string, optional) — Whether to include sticker models with the response
- `sticker_fields` (query, string, optional) — all or a comma-separated list of sticker fields
- `customFieldItems` (query, string, optional) — Whether to include the customFieldItems

## Original description

Get a card by its ID
