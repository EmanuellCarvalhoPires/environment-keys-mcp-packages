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
path: "/snippets/{workspace}/{encoded_id}/{node_id}/files/{path}"
category: "Snippets"
writes_data: false
tool_note: "[[bitbucket_get_a_snippet_s_raw_file]]"
---
# Bitbucket - Get a snippet's raw file

**Get a snippet's raw file** — `GET /snippets/{workspace}/{encoded_id}/{node_id}/files/{path}`

- Run by the tool [[bitbucket_get_a_snippet_s_raw_file]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}/{{param:node_id}}/files/{{param:path}}
Authorization: {{service.auth_token}}
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.
- `node_id` (path, string, required) — Value of nodeid in the path.
- `path` (path, string, required) — Value of path in the path.

## Original description

Retrieves the raw contents of a specific file in the snippet. The
`Content-Disposition` header will be "attachment" to avoid issues with
malevolent executable files.

The file's mime type is derived from its filename and returned in the
`Content-Type` header.

Note that for text files, no character encoding is included as part of
the content type.
