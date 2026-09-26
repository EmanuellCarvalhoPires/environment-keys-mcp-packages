---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/boards/{id}/exports/{idExport}/download"
category: "Boards"
writes_data: false
---
# Trello - Download an Export for a Board

**Download an Export for a Board** — `GET /boards/{id}/exports/{idExport}/download`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Download an Export for a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/boards/{{param:id}}/exports/{{param:idExport}}/download
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idExport` (path, string, required) — Value of idExport in the path.

## Original description

Download the exported file. Redirects to the file location if the export is ready, or errors if it is not.
