---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/organizations
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/organizations/{id}/exports"
category: "Organizations"
writes_data: true
---
# Trello - Create Export for Organizations

**Create Export for Organizations** — `POST /organizations/{id}/exports`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create Export for Organizations"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/organizations/{{param:id}}/exports?attachments={{param:attachments}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `attachments` (query, string, optional) — Whether the CSV should include attachments or not.

## Original description

Kick off CSV export for an organization
