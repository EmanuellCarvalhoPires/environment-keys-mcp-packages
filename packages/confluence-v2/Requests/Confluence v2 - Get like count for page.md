---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/like
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/pages/{id}/likes/count"
category: "Like"
writes_data: false
tool_note: "[[confluence_get_like_count_for_page]]"
---
# Confluence v2 - Get like count for page

**Get like count for page** — `GET /pages/{id}/likes/count`

- Run by the tool [[confluence_get_like_count_for_page]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/pages/{{param:id}}/likes/count
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the page for which like count should be returned.

## Original description

Returns the count of likes of specific page.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content of the page and its corresponding space.
