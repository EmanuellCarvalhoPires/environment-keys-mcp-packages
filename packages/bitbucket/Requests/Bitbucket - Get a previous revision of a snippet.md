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
path: "/snippets/{workspace}/{encoded_id}/{node_id}"
category: "Snippets"
writes_data: false
tool_note: "[[bitbucket_get_a_previous_revision_of_a_snippet]]"
---
# Bitbucket - Get a previous revision of a snippet

**Get a previous revision of a snippet** — `GET /snippets/{workspace}/{encoded_id}/{node_id}`

- Run by the tool [[bitbucket_get_a_previous_revision_of_a_snippet]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}/{{param:node_id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.
- `node_id` (path, string, required) — Value of nodeid in the path.

## Original description

Identical to `GET /snippets/encoded_id`, except that this endpoint
can be used to retrieve the contents of the snippet as it was at an
older revision, while `/snippets/encoded_id` always returns the
snippet's current revision.

Note that only the snippet's file contents are versioned, not its
meta data properties like the title.

Other than that, the two endpoints are identical in behavior.
