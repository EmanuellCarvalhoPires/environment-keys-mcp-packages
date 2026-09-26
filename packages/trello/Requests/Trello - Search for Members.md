---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/search
  - api/operation/search
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/search/members/"
category: "Search"
writes_data: false
---
# Trello - Search for Members

**Search for Members** — `GET /search/members/`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Search for Members"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/search/members/?query={{param:query}}&limit={{param:limit}}&idBoard={{param:idBoard}}&idOrganization={{param:idOrganization}}&onlyOrgMembers={{param:onlyOrgMembers}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `query` (query, string, required) — Search query 1 to 16384 characters long
- `limit` (query, string, optional) — The maximum number of results to return. Maximum of 20.
- `idBoard` (query, string, optional) — Query parameter idBoard.
- `idOrganization` (query, string, optional) — Query parameter idOrganization.
- `onlyOrgMembers` (query, string, optional) — Query parameter onlyOrgMembers.

## Original description

Search for Trello members.
