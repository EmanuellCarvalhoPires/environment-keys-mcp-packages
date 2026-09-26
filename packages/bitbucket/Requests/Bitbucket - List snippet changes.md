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
path: "/snippets/{workspace}/{encoded_id}/commits"
category: "Snippets"
writes_data: false
tool_note: "[[bitbucket_list_snippet_changes]]"
---
# Bitbucket - List snippet changes

**List snippet changes** — `GET /snippets/{workspace}/{encoded_id}/commits`

- Run by the tool [[bitbucket_list_snippet_changes]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}/commits
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.

## Original description

Returns the changes (commits) made on this snippet.
