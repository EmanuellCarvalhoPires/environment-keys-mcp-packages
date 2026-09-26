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
path: "/snippets/{workspace}/{encoded_id}/watch"
category: "Snippets"
writes_data: true
tool_note: "[[bitbucket_watch_a_snippet]]"
---
# Bitbucket - Watch a snippet

**Watch a snippet** — `PUT /snippets/{workspace}/{encoded_id}/watch`

- Run by the tool [[bitbucket_watch_a_snippet]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}/watch
Authorization: {{service.auth_token}}
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.

## Original description

Used to start watching a specific snippet. Returns 204 (No Content).
