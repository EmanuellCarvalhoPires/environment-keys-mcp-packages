---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commit-statuses
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses"
category: "Commit statuses"
writes_data: false
tool_note: "[[bitbucket_list_commit_statuses_for_a_commit]]"
---
# Bitbucket - List commit statuses for a commit

**List commit statuses for a commit** — `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses`

- Run by the tool [[bitbucket_list_commit_statuses_for_a_commit]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commit/{{param:commit}}/statuses?refname={{param:refname}}&q={{param:q}}&sort={{param:sort}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `commit` (path, string, required) — Value of commit in the path.
- `refname` (query, string, optional) — If specified, only return commit status objects that were either created without a refname, or were created with the specified refname
- `q` (query, string, optional) — Query string to narrow down the response as per filtering and sorting.
- `sort` (query, string, optional) — Field by which the results should be sorted as per filtering and sorting. Defaults to createdon.

## Original description

Returns all statuses (e.g. build results) for a specific commit.
