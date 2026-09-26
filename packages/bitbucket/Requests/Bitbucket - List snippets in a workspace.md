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
path: "/snippets/{workspace}"
category: "Snippets"
writes_data: false
tool_note: "[[bitbucket_list_snippets_in_a_workspace]]"
---
# Bitbucket - List snippets in a workspace

**List snippets in a workspace** — `GET /snippets/{workspace}`

- Run by the tool [[bitbucket_list_snippets_in_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/snippets/{{service.workspace}}?role={{param:role}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `role` (query, string, optional) — Filter down the result based on the authenticated user's role (owner, contributor, or member).

## Original description

Returns a paginated list of snippets owned by `{workspace}`.

To limit the set of returned snippets, apply the
`?role=[owner|contributor|member]` query parameter where the roles are
defined as follows:

* `owner`: snippets owned by `{workspace}` that also belong to the current user
    (only returns results when `{workspace}` is the current user's personal workspace)
* `contributor`: snippets owned by `{workspace}` that the current user is watching,
    plus any owned by `{workspace}` and the current user
* `member`: all snippets owned by `{workspace}` if the current user is a member,
    otherwise only those the current user is watching

When no role is specified, all snippets owned by `{workspace}` are returned.

If the current user is not a member of `{workspace}`, only public snippets are
returned regardless of role.

The returned response is a normal paginated JSON list. This endpoint
only supports `application/json` responses and no
`multipart/form-data` or `multipart/related`. As a result, it is not
possible to include the file contents.
