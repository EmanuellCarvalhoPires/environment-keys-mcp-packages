---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/snippets/{workspace}/{encoded_id}/comments/{comment_id}"
category: "Snippets"
writes_data: false
tool_note: "[[bitbucket_get_a_comment_on_a_snippet]]"
---
# Bitbucket - Get a comment on a snippet

**Get a comment on a snippet** — `GET /snippets/{workspace}/{encoded_id}/comments/{comment_id}`

- Run by the tool [[bitbucket_get_a_comment_on_a_snippet]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}/comments/{{param:comment_id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.
- `comment_id` (path, string, required) — Value of commentid in the path.

## Original description

Returns the specific snippet comment.
