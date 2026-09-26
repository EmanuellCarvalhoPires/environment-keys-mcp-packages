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
path: "/snippets/{workspace}/{encoded_id}/watch"
category: "Snippets"
writes_data: true
tool_note: "[[bitbucket_stop_watching_a_snippet]]"
---
# Bitbucket - Stop watching a snippet

**Stop watching a snippet** — `DELETE /snippets/{workspace}/{encoded_id}/watch`

- Run by the tool [[bitbucket_stop_watching_a_snippet]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}/watch
Authorization: {{service.auth_token}}
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.

## Original description

Used to stop watching a specific snippet. Returns 204 (No Content)
to indicate success.
