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
path: "/enterprises/{id}/claimableOrganizations"
category: "Enterprises"
writes_data: false
---
# Trello - Get ClaimableOrganizations of an Enterprise

**Get ClaimableOrganizations of an Enterprise** — `GET /enterprises/{id}/claimableOrganizations`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get ClaimableOrganizations of an Enterprise"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/enterprises/{{param:id}}/claimableOrganizations?limit={{param:limit}}&cursor={{param:cursor}}&name={{param:name}}&activeSince={{param:activeSince}}&inactiveSince={{param:inactiveSince}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — ID of the enterprise to retrieve
- `limit` (query, string, optional) — Limits the number of workspaces to be sorted
- `cursor` (query, string, optional) — Specifies the sort order to return matching documents
- `name` (query, string, optional) — Name of the enterprise to retrieve workspaces for
- `activeSince` (query, string, optional) — Date in YYYY-MM-DD format indicating the date to search up to for activeness of workspace
- `inactiveSince` (query, string, optional) — Date in YYYY-MM-DD format indicating the date to search up to for inactiveness of workspace

## Original description

Get the Workspaces that are claimable by the enterprise by ID. Can optionally query for workspaces based on activeness/ inactiveness.
