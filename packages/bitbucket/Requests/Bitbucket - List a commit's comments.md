---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/commit/{commit}/comments"
category: "Commits"
writes_data: false
tool_note: "[[bitbucket_list_a_commit_s_comments]]"
---
# Bitbucket - List a commit's comments

**List a commit's comments** — `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/comments`

- Run by the tool [[bitbucket_list_a_commit_s_comments]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commit/{{param:commit}}/comments?q={{param:q}}&sort={{param:sort}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `commit` (path, string, required) — Value of commit in the path.
- `q` (query, string, optional) — Query string to narrow down the response as per filtering and sorting.
- `sort` (query, string, optional) — Field by which the results should be sorted as per filtering and sorting.

## Original description

Returns the commit's comments.

This includes both global and inline comments.

The default sorting is oldest to newest and can be overridden with
the `sort` query parameter.
