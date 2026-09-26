---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/snippets/{workspace}/{encoded_id}/{node_id}"
category: "Snippets"
writes_data: true
tool_note: "[[bitbucket_update_a_previous_revision_of_a_snippet]]"
---
# Bitbucket - Update a previous revision of a snippet

**Update a previous revision of a snippet** — `PUT /snippets/{workspace}/{encoded_id}/{node_id}`

- Run by the tool [[bitbucket_update_a_previous_revision_of_a_snippet]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}/{{param:node_id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.
- `node_id` (path, string, required) — Value of nodeid in the path.

## Original description

Identical to `UPDATE /snippets/encoded_id`, except that this endpoint
takes an explicit commit revision. Only the snippet's "HEAD"/"tip"
(most recent) version can be updated and requests on all other,
older revisions fail by returning a 405 status.

Usage of this endpoint over the unrestricted `/snippets/encoded_id`
could be desired if the caller wants to be sure no concurrent
modifications have taken place between the moment of the UPDATE
request and the original GET.

This can be considered a so-called "Compare And Swap", or CAS
operation.

Other than that, the two endpoints are identical in behavior.
