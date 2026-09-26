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
path: "/snippets/{workspace}/{encoded_id}/watch"
category: "Snippets"
writes_data: false
tool_note: "[[bitbucket_check_if_the_current_user_is_watching_a_snippet]]"
---
# Bitbucket - Check if the current user is watching a snippet

**Check if the current user is watching a snippet** — `GET /snippets/{workspace}/{encoded_id}/watch`

- Run by the tool [[bitbucket_check_if_the_current_user_is_watching_a_snippet]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}/watch
Authorization: {{service.auth_token}}
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.

## Original description

Used to check if the current user is watching a specific snippet.

Returns 204 (No Content) if the user is watching the snippet and 404 if
not.

Hitting this endpoint anonymously always returns a 404.
