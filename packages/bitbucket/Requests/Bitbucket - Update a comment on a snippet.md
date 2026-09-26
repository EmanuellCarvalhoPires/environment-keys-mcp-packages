---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/snippets/{workspace}/{encoded_id}/comments/{comment_id}"
category: "Snippets"
writes_data: true
tool_note: "[[bitbucket_update_a_comment_on_a_snippet]]"
---
# Bitbucket - Update a comment on a snippet

**Update a comment on a snippet** — `PUT /snippets/{workspace}/{encoded_id}/comments/{comment_id}`

- Run by the tool [[bitbucket_update_a_comment_on_a_snippet]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}/comments/{{param:comment_id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.
- `comment_id` (path, string, required) — Value of commentid in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates a comment.

The only required field in the body is `content.raw`.

Comments can only be updated by their author.
