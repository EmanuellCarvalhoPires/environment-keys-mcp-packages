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
path: "/enterprises/{id}/pendingOrganizations"
category: "Enterprises"
writes_data: false
---
# Trello - Get PendingOrganizations of an Enterprise

**Get PendingOrganizations of an Enterprise** — `GET /enterprises/{id}/pendingOrganizations`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get PendingOrganizations of an Enterprise"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/enterprises/{{param:id}}/pendingOrganizations?activeSince={{param:activeSince}}&inactiveSince={{param:inactiveSince}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — ID of the enterprise to retrieve
- `activeSince` (query, string, optional) — Date in YYYY-MM-DD format indicating the date to search up to for activeness of workspace
- `inactiveSince` (query, string, optional) — Date in YYYY-MM-DD format indicating the date to search up to for inactiveness of workspace

## Original description

Get the Workspaces that are pending for the enterprise by ID.
