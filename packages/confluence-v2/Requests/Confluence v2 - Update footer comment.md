---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/comment
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: PUT
path: "/footer-comments/{comment-id}"
category: "Comment"
writes_data: true
tool_note: "[[confluence_update_footer_comment]]"
---
# Confluence v2 - Update footer comment

**Update footer comment** — `PUT /footer-comments/{comment-id}`

- Run by the tool [[confluence_update_footer_comment]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
PUT {{service.url}}/wiki/api/v2/footer-comments/{{param:comment_id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `comment_id` (path, string, required) — The ID of the comment to be retrieved.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update a footer comment. This can be used to update the body text of a comment.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content of the page or blogpost and its corresponding space. Permission to create comments in the space.
