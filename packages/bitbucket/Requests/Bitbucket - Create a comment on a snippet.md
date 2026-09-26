---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/snippets/{workspace}/{encoded_id}/comments"
category: "Snippets"
writes_data: true
tool_note: "[[bitbucket_create_a_comment_on_a_snippet]]"
---
# Bitbucket - Create a comment on a snippet

**Create a comment on a snippet** — `POST /snippets/{workspace}/{encoded_id}/comments`

- Run by the tool [[bitbucket_create_a_comment_on_a_snippet]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}/comments
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new comment.

The only required field in the body is `content.raw`.

To create a threaded reply to an existing comment, include `parent.id`.
