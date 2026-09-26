---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/comment
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: DELETE
path: "/inline-comments/{comment-id}"
category: "Comment"
writes_data: true
tool_note: "[[confluence_delete_inline_comment]]"
---
# Confluence v2 - Delete inline comment

**Delete inline comment** — `DELETE /inline-comments/{comment-id}`

- Run by the tool [[confluence_delete_inline_comment]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
DELETE {{service.url}}/wiki/api/v2/inline-comments/{{param:comment_id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `comment_id` (path, string, required) — The ID of the comment to be deleted.

## Original description

Deletes an inline comment. This is a permanent deletion and cannot be reverted.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content of the page or blogpost and its corresponding space. Permission to delete comments in the space.
