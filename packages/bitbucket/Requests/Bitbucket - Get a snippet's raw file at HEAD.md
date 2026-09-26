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
path: "/snippets/{workspace}/{encoded_id}/files/{path}"
category: "Snippets"
writes_data: false
tool_note: "[[bitbucket_get_a_snippet_s_raw_file_at_head]]"
---
# Bitbucket - Get a snippet's raw file at HEAD

**Get a snippet's raw file at HEAD** — `GET /snippets/{workspace}/{encoded_id}/files/{path}`

- Run by the tool [[bitbucket_get_a_snippet_s_raw_file_at_head]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}/files/{{param:path}}
Authorization: {{service.auth_token}}
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.
- `path` (path, string, required) — Value of path in the path.

## Original description

Convenience resource for getting to a snippet's raw files without the
need for first having to retrieve the snippet itself and having to pull
out the versioned file links.
