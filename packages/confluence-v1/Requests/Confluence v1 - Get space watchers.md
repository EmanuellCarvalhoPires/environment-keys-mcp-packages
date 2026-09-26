---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-watches
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/space/{spaceKey}/watch"
category: "Content watches"
writes_data: false
tool_note: "[[confluence_v1_get_space_watchers]]"
---
# Confluence v1 - Get space watchers

**Get space watchers** — `GET /wiki/rest/api/space/{spaceKey}/watch`

- Run by the tool [[confluence_v1_get_space_watchers]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/space/{{param:spaceKey}}/watch?start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `spaceKey` (path, string, required) — The key of the space to get watchers.
- `start` (query, string, optional) — The start point of the collection to return.
- `limit` (query, string, optional) — The limit of the number of items to return, this may be restricted by fixed system limits.

## Original description

Returns a list of watchers of a space
