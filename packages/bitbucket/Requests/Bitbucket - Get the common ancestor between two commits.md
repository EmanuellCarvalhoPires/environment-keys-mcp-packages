---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/merge-base/{revspec}"
category: "Commits"
writes_data: false
tool_note: "[[bitbucket_get_the_common_ancestor_between_two_commits]]"
---
# Bitbucket - Get the common ancestor between two commits

**Get the common ancestor between two commits** — `GET /repositories/{workspace}/{repo_slug}/merge-base/{revspec}`

- Run by the tool [[bitbucket_get_the_common_ancestor_between_two_commits]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/merge-base/{{param:revspec}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `revspec` (path, string, required) — Value of revspec in the path.

## Original description

Returns the best common ancestor between two commits, specified in a revspec
of 2 commits (e.g. 3a8b42..9ff173).

If more than one best common ancestor exists, only one will be returned. It is
unspecified which will be returned.
