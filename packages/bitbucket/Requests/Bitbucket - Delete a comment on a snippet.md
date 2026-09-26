---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/snippets/{workspace}/{encoded_id}/comments/{comment_id}"
category: "Snippets"
writes_data: true
tool_note: "[[bitbucket_delete_a_comment_on_a_snippet]]"
---
# Bitbucket - Delete a comment on a snippet

**Delete a comment on a snippet** — `DELETE /snippets/{workspace}/{encoded_id}/comments/{comment_id}`

- Run by the tool [[bitbucket_delete_a_comment_on_a_snippet]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}/comments/{{param:comment_id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.
- `comment_id` (path, string, required) — Value of commentid in the path.

## Original description

Deletes a snippet comment.

Comments can only be removed by the comment author, snippet creator, or workspace admin.
