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
path: "/snippets/{workspace}"
category: "Snippets"
writes_data: true
tool_note: "[[bitbucket_create_a_snippet_for_a_workspace]]"
---
# Bitbucket - Create a snippet for a workspace

**Create a snippet for a workspace** — `POST /snippets/{workspace}`

- Run by the tool [[bitbucket_create_a_snippet_for_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/snippets/{{service.workspace}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Identical to [`/snippets`](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-post), except that the new snippet will be
created under the workspace specified in the path parameter
`{workspace}`.
