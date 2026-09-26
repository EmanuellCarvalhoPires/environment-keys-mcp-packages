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
path: "/inline-comments/{id}/likes/count"
category: "Like"
writes_data: false
tool_note: "[[confluence_get_like_count_for_inline_comment]]"
---
# Confluence v2 - Get like count for inline comment

**Get like count for inline comment** — `GET /inline-comments/{id}/likes/count`

- Run by the tool [[confluence_get_like_count_for_inline_comment]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/inline-comments/{{param:id}}/likes/count
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the inline comment for which like count should be returned.

## Original description

Returns the count of likes of specific inline comment.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content of the page/blogpost and its corresponding space.
