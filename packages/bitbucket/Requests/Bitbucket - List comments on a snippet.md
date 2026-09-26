---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/snippets/{workspace}/{encoded_id}/comments"
category: "Snippets"
writes_data: false
tool_note: "[[bitbucket_list_comments_on_a_snippet]]"
---
# Bitbucket - List comments on a snippet

**List comments on a snippet** — `GET /snippets/{workspace}/{encoded_id}/comments`

- Run by the tool [[bitbucket_list_comments_on_a_snippet]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}/comments
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.

## Original description

Used to retrieve a paginated list of all comments for a specific
snippet.

This resource works identical to commit and pull request comments.

The default sorting is oldest to newest and can be overridden with
the `sort` query parameter.
