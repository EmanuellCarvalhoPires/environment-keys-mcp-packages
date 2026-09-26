---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/cards
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/cards"
category: "Cards"
writes_data: true
---
# Trello - Create a new Card

**Create a new Card** — `POST /cards`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create a new Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/cards?name={{param:name}}&desc={{param:desc}}&pos={{param:pos}}&due={{param:due}}&start={{param:start}}&dueComplete={{param:dueComplete}}&idList={{param:idList}}&idMembers={{param:idMembers}}&idLabels={{param:idLabels}}&urlSource={{param:urlSource}}&fileSource={{param:fileSource}}&mimeType={{param:mimeType}}&idCardSource={{param:idCardSource}}&keepFromSource={{param:keepFromSource}}&address={{param:address}}&locationName={{param:locationName}}&coordinates={{param:coordinates}}&cardRole={{param:cardRole}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `name` (query, string, optional) — The name for the card
- `desc` (query, string, optional) — The description for the card
- `pos` (query, string, optional) — The position of the new card. top, bottom, or a positive float
- `due` (query, string, optional) — A due date for the card
- `start` (query, string, optional) — The start date of a card, or null
- `dueComplete` (query, string, optional) — Whether the status of the card is complete
- `idList` (query, string, required) — The ID of the list the card should be created in
- `idMembers` (query, string, optional) — Comma-separated list of member IDs to add to the card
- `idLabels` (query, string, optional) — Comma-separated list of label IDs to add to the card
- `urlSource` (query, string, optional) — A URL starting with http:// or https://. The URL will be attached to the card upon creation.
- `fileSource` (query, string, optional) — Query parameter fileSource.
- `mimeType` (query, string, optional) — The mimeType of the attachment. Max length 256
- `idCardSource` (query, string, optional) — The ID of a card to copy into the new card
- `keepFromSource` (query, string, optional) — If using idCardSource you can specify which properties to copy over. all or comma-separated list of: attachments,checklists,customFields,comments,due,start,labels,members,start,stickers
- `address` (query, string, optional) — For use with/by the Map View
- `locationName` (query, string, optional) — For use with/by the Map View
- `coordinates` (query, string, optional) — For use with/by the Map View. Should take the form latitude,longitude
- `cardRole` (query, string, optional) — For displaying cards in different ways based on the card name. Board cards must have a name that is a link to a Trello board. Mirror cards must have a name that is a link to a Trello card.

## Original description

Create a new card. Query parameters may also be replaced with a JSON request body instead.
