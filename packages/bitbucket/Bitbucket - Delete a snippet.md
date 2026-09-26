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
path: "/snippets/{workspace}/{encoded_id}"
category: "Snippets"
writes_data: true
tool_note: "[[bitbucket_delete_a_snippet]]"
---
# Bitbucket - Delete a snippet

**Delete a snippet** — `DELETE /snippets/{workspace}/{encoded_id}`

- Run by the tool [[bitbucket_delete_a_snippet]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.

## Original description

Deletes a snippet and returns an empty response.
