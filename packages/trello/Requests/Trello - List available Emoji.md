---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/emoji
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/emoji"
category: "Emoji"
writes_data: false
---
# Trello - List available Emoji

**List available Emoji** — `GET /emoji`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - List available Emoji"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/emoji?locale={{param:locale}}&spritesheets={{param:spritesheets}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `locale` (query, string, optional) — The locale to return emoji descriptions and names in. Defaults to the logged in member's locale.
- `spritesheets` (query, string, optional) — true to return spritesheet URLs in the response

## Original description

List available Emoji
