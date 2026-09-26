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
path: "/footer-comments/{id}/likes/users"
category: "Like"
writes_data: false
tool_note: "[[confluence_get_account_ids_of_likes_for_footer_comment]]"
---
# Confluence v2 - Get account IDs of likes for footer comment

**Get account IDs of likes for footer comment** — `GET /footer-comments/{id}/likes/users`

- Run by the tool [[confluence_get_account_ids_of_likes_for_footer_comment]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/footer-comments/{{param:id}}/likes/users?cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the footer comment for which like count should be returned.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of account IDs per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results.

## Original description

Returns the account IDs of likes of specific footer comment.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content of the page/blogpost and its corresponding space.
