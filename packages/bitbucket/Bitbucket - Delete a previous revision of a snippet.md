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
path: "/snippets/{workspace}/{encoded_id}/{node_id}"
category: "Snippets"
writes_data: true
tool_note: "[[bitbucket_delete_a_previous_revision_of_a_snippet]]"
---
# Bitbucket - Delete a previous revision of a snippet

**Delete a previous revision of a snippet** — `DELETE /snippets/{workspace}/{encoded_id}/{node_id}`

- Run by the tool [[bitbucket_delete_a_previous_revision_of_a_snippet]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}/{{param:node_id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.
- `node_id` (path, string, required) — Value of nodeid in the path.

## Original description

Deletes the snippet.

Note that this only works for versioned URLs that point to the latest
commit of the snippet. Pointing to an older commit results in a 405
status code.

To delete a snippet, regardless of whether or not concurrent changes
are being made to it, use `DELETE /snippets/{encoded_id}` instead.
