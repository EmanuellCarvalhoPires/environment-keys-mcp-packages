---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/boards/{id}/exports"
category: "Boards"
writes_data: true
---
# Trello - Create an Export for a Board

**Create an Export for a Board** — `POST /boards/{id}/exports`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create an Export for a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/boards/{{param:id}}/exports?attachments={{param:attachments}}&attachment_age={{param:attachment_age}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `attachments` (query, string, optional) — Whether the export should include attachments
- `attachment_age` (query, string, optional) — Only include attachments created within this many days. 0 means no limit.

## Original description

Kick off an export of a board. Only one export may be in progress for a board at a time.
