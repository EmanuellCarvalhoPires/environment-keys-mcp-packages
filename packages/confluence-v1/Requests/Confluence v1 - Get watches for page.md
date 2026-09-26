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
path: "/wiki/rest/api/content/{id}/notification/child-created"
category: "Content watches"
writes_data: false
tool_note: "[[confluence_v1_get_watches_for_page]]"
---
# Confluence v1 - Get watches for page

**Get watches for page** — `GET /wiki/rest/api/content/{id}/notification/child-created`

- Run by the tool [[confluence_v1_get_watches_for_page]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/content/{{param:id}}/notification/child-created?start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the content to be queried for its watches.
- `start` (query, string, optional) — The starting index of the returned watches.
- `limit` (query, string, optional) — The maximum number of watches to return per page. Note, this may be restricted by fixed system limits.

## Original description

Returns the watches for a page. A user that watches a page will receive
receive notifications when the page is updated.

If you want to manage watches for a page, use the following `user` methods:

- [Get content watch status for user](#api-user-watch-content-contentId-get)
- [Add content watch](#api-user-watch-content-contentId-post)
- [Remove content watch](#api-user-watch-content-contentId-delete)

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
