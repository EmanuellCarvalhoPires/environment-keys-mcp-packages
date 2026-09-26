---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/notifications
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/notifications/{id}"
category: "Notifications"
writes_data: false
---
# Trello - Get a Notification

**Get a Notification** — `GET /notifications/{id}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Notification"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/notifications/{{param:id}}?board={{param:board}}&board_fields={{param:board_fields}}&card={{param:card}}&card_fields={{param:card_fields}}&display={{param:display}}&entities={{param:entities}}&fields={{param:fields}}&list={{param:list}}&member={{param:member}}&member_fields={{param:member_fields}}&memberCreator={{param:memberCreator}}&memberCreator_fields={{param:memberCreator_fields}}&organization={{param:organization}}&organization_fields={{param:organization_fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the notification
- `board` (query, string, optional) — Whether to include the board object
- `board_fields` (query, string, optional) — all or a comma-separated list of board fields
- `card` (query, string, optional) — Whether to include the card object
- `card_fields` (query, string, optional) — all or a comma-separated list of card fields
- `display` (query, string, optional) — Whether to include the display object with the results
- `entities` (query, string, optional) — Whether to include the entities object with the results
- `fields` (query, string, optional) — all or a comma-separated list of notification fields
- `list` (query, string, optional) — Whether to include the list object
- `member` (query, string, optional) — Whether to include the member object
- `member_fields` (query, string, optional) — all or a comma-separated list of member fields
- `memberCreator` (query, string, optional) — Whether to include the member object of the creator
- `memberCreator_fields` (query, string, optional) — all or a comma-separated list of member fields
- `organization` (query, string, optional) — Whether to include the organization object
- `organization_fields` (query, string, optional) — all or a comma-separated list of organization fields

