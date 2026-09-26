---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/enterprises
  - api/operation/search
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/enterprises/{id}/members/query"
category: "Enterprises"
writes_data: false
---
# Trello - Get Users of an Enterprise

**Get Users of an Enterprise** — `GET /enterprises/{id}/members/query`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Users of an Enterprise"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/enterprises/{{param:id}}/members/query?licensed={{param:licensed}}&deactivated={{param:deactivated}}&collaborator={{param:collaborator}}&managed={{param:managed}}&admin={{param:admin}}&activeSince={{param:activeSince}}&inactiveSince={{param:inactiveSince}}&search={{param:search}}&cursor={{param:cursor}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — ID of the enterprise to retrieve.
- `licensed` (query, string, optional) — When true, returns members who possess a license for the corresponding Trello Enterprise; when false, returns members who do not. If unspecified, both licensed and unlicensed members will be returned.
- `deactivated` (query, string, optional) — When true, returns members who have been deactivated for the corresponding Trello Enterprise; when false, returns members who have not.
- `collaborator` (query, string, optional) — When true, returns members who are guests on one or more boards in the corresponding Trello Enterprise (but do not possess a license); when false, returns members who are not.
- `managed` (query, string, optional) — When true, returns members who are managed by the corresponding Trello Enterprise; when false, returns members who are not. If unspecified, both managed and unmanaged members will be returned.
- `admin` (query, string, optional) — When true, returns members who are administrators of the corresponding Trello Enterprise; when false, returns members who are not. If unspecified, both admin and non-admin members will be returned.
- `activeSince` (query, string, optional) — Returns only Trello users active since this date (inclusive).
- `inactiveSince` (query, string, optional) — Returns only Trello users active since this date (inclusive).
- `search` (query, string, optional) — Returns members with email address or full name that start with the search value.
- `cursor` (query, string, optional) — Cursor to return next set of results, use cursor returned in the response to query the next batch.

## Original description

Get an enterprise's users. You can choose to retrieve licensed members, board guests, etc. The response is paginated and will return 100 users at a time.
