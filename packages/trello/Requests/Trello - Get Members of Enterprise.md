---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/enterprises
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/enterprises/{id}/members"
category: "Enterprises"
writes_data: false
---
# Trello - Get Members of Enterprise

**Get Members of Enterprise** — `GET /enterprises/{id}/members`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Members of Enterprise"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/enterprises/{{param:id}}/members?fields={{param:fields}}&filter={{param:filter}}&sort={{param:sort}}&sortBy={{param:sortBy}}&sortOrder={{param:sortOrder}}&startIndex={{param:startIndex}}&count={{param:count}}&organization_fields={{param:organization_fields}}&board_fields={{param:board_fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — ID of the Enterprise to retrieve.
- `fields` (query, string, optional) — A comma-seperated list of valid member fields.
- `filter` (query, string, optional) — Pass a SCIM-style query to filter members. This takes precedence over the all/normal/admins value of members. If any of the below member args are set, the member array will be paginated.
- `sort` (query, string, optional) — This parameter expects a SCIM-style sorting value prefixed by a - to sort descending. If no - is prefixed, it will be sorted ascending.
- `sortBy` (query, string, optional) — Deprecated: Please use sort instead. This parameter expects a SCIM-style sorting value. Note that the members array returned will be paginated if members is 'normal' or 'admins'.
- `sortOrder` (query, string, optional) — Deprecated: Please use sort instead. One of: ascending, descending, asc, desc.
- `startIndex` (query, string, optional) — Any integer between 0 and 9999.
- `count` (query, string, optional) — SCIM-style filter.
- `organization_fields` (query, string, optional) — Any valid value that the nested organization field resource accepts.
- `board_fields` (query, string, optional) — Any valid value that the nested board resource accepts.

## Original description

Get the members of an enterprise.
