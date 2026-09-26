---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/members/{id}/boards"
category: "Members"
writes_data: false
---
# Trello - Get Boards that Member belongs to

**Get Boards that Member belongs to** — `GET /members/{id}/boards`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Boards that Member belongs to"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/boards?filter={{param:filter}}&fields={{param:fields}}&lists={{param:lists}}&organization={{param:organization}}&organization_fields={{param:organization_fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or username of the member
- `filter` (query, string, optional) — all or a comma-separated list of: closed, members, open, organization, public, starred
- `fields` (query, string, optional) — all or a comma-separated list of board fields
- `lists` (query, string, optional) — Which lists to include with the boards. One of: all, closed, none, open
- `organization` (query, string, optional) — Whether to include the Organization object with the Boards
- `organization_fields` (query, string, optional) — all or a comma-separated list of organization fields

## Original description

Lists the boards that the user is a member of.
