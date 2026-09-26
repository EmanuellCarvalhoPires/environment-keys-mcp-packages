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
path: "/snippets/{workspace}/{encoded_id}/commits/{revision}"
category: "Snippets"
writes_data: false
tool_note: "[[bitbucket_get_a_previous_snippet_change]]"
---
# Bitbucket - Get a previous snippet change

**Get a previous snippet change** — `GET /snippets/{workspace}/{encoded_id}/commits/{revision}`

- Run by the tool [[bitbucket_get_a_previous_snippet_change]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}/commits/{{param:revision}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.
- `revision` (path, string, required) — Value of revision in the path.

## Original description

Returns the changes made on this snippet in this commit.
