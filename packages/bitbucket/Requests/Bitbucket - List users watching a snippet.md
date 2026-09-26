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
path: "/snippets/{workspace}/{encoded_id}/watchers"
category: "Snippets"
writes_data: false
tool_note: "[[bitbucket_list_users_watching_a_snippet]]"
---
# Bitbucket - List users watching a snippet

**List users watching a snippet** — `GET /snippets/{workspace}/{encoded_id}/watchers`

- Run by the tool [[bitbucket_list_users_watching_a_snippet]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}/watchers
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.

## Original description

Returns a paginated list of all users watching a specific snippet.
