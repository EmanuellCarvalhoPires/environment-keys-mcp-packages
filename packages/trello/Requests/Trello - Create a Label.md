---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/labels
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/labels"
category: "Labels"
writes_data: true
---
# Trello - Create a Label

**Create a Label** — `POST /labels`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create a Label"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/labels?name={{param:name}}&color={{param:color}}&idBoard={{param:idBoard}}
Authorization: {{service.auth_token}}
```

## Parameters

- `name` (query, string, required) — Name for the label
- `color` (query, string, required) — The color for the label.
- `idBoard` (query, string, required) — The ID of the Board to create the Label on.

## Original description

Create a new Label on a Board.
