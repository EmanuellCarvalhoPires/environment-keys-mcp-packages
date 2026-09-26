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
path: "/wiki/rest/api/content/{id}/notification/created"
category: "Content watches"
writes_data: false
tool_note: "[[confluence_v1_get_watches_for_space]]"
---
# Confluence v1 - Get watches for space

**Get watches for space** — `GET /wiki/rest/api/content/{id}/notification/created`

- Run by the tool [[confluence_v1_get_watches_for_space]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/content/{{param:id}}/notification/created?start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the content to be queried for its watches.
- `start` (query, string, optional) — The starting index of the returned watches.
- `limit` (query, string, optional) — The maximum number of watches to return per page. Note, this may be restricted by fixed system limits.

## Original description

Returns all space watches for the space that the content is in. A user that
watches a space will receive receive notifications when any content in the
space is updated.

If you want to manage watches for a space, use the following `user` methods:

- [Get space watch status for user](#api-user-watch-space-spaceKey-get)
- [Add space watch](#api-user-watch-space-spaceKey-post)
- [Remove space watch](#api-user-watch-space-spaceKey-delete)

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
