---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/cards
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/cards/{id}"
category: "Cards"
writes_data: true
---
# Trello - Update a Card

**Update a Card** — `PUT /cards/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/cards/{{param:id}}?name={{param:name}}&desc={{param:desc}}&closed={{param:closed}}&idMembers={{param:idMembers}}&idAttachmentCover={{param:idAttachmentCover}}&idList={{param:idList}}&idLabels={{param:idLabels}}&idBoard={{param:idBoard}}&pos={{param:pos}}&due={{param:due}}&start={{param:start}}&dueComplete={{param:dueComplete}}&subscribed={{param:subscribed}}&address={{param:address}}&locationName={{param:locationName}}&coordinates={{param:coordinates}}&cover={{param:cover}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `name` (query, string, optional) — The new name for the card
- `desc` (query, string, optional) — The new description for the card
- `closed` (query, string, optional) — Whether the card should be archived (closed: true)
- `idMembers` (query, string, optional) — Comma-separated list of member IDs
- `idAttachmentCover` (query, string, optional) — The ID of the image attachment the card should use as its cover, or null for none
- `idList` (query, string, optional) — The ID of the list the card should be in
- `idLabels` (query, string, optional) — Comma-separated list of label IDs
- `idBoard` (query, string, optional) — The ID of the board the card should be on
- `pos` (query, string, optional) — The position of the card in its list. top, bottom, or a positive float
- `due` (query, string, optional) — When the card is due, or null
- `start` (query, string, optional) — The start date of a card, or null
- `dueComplete` (query, string, optional) — Whether the status of the card is complete
- `subscribed` (query, string, optional) — Whether the member is should be subscribed to the card
- `address` (query, string, optional) — For use with/by the Map View
- `locationName` (query, string, optional) — For use with/by the Map View
- `coordinates` (query, string, optional) — For use with/by the Map View. Should be latitude,longitude
- `cover` (query, string, optional) — Updates the card's cover | Option | Values | About | |--------|--------|-------| | color | pink, yellow, lime, blue, black, orange, red, purple, sky, green | Makes the cover a solid color .

## Original description

Update a card. Query parameters may also be replaced with a JSON request body instead.
