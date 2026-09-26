---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/plugins
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/plugins/{idPlugin}/listings/{idListing}"
category: "Plugins"
writes_data: true
---
# Trello - Updating Plugin's Listing

**Updating Plugin's Listing** — `PUT /plugins/{idPlugin}/listings/{idListing}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Updating Plugin's Listing"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/plugins/{{param:idPlugin}}/listings/{{param:idListing}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `idPlugin` (path, string, required) — The ID of the Power-Up whose listing is being updated.
- `idListing` (path, string, required) — The ID of the existing listing for the Power-Up that is being updated.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update an existing listing for your Power-Up
