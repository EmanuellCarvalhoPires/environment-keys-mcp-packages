---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/plugins
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/plugins/{idPlugin}/listings"
category: "Plugins"
writes_data: true
---
# Trello - Create a Listing for Plugin

**Create a Listing for Plugin** — `POST /plugins/{idPlugin}/listings`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create a Listing for Plugin"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/plugins/{{param:idPlugin}}/listings
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `idPlugin` (path, string, required) — The ID of the Power-Up for which you are creating a new listing.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create a new listing for a given locale for your Power-Up
