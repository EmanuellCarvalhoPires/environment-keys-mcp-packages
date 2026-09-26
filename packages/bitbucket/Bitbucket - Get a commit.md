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
path: "/repositories/{workspace}/{repo_slug}/commit/{commit}"
category: "Commits"
writes_data: false
tool_note: "[[bitbucket_get_a_commit]]"
---
# Bitbucket - Get a commit

**Get a commit** — `GET /repositories/{workspace}/{repo_slug}/commit/{commit}`

- Run by the tool [[bitbucket_get_a_commit]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commit/{{param:commit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `commit` (path, string, required) — Value of commit in the path.

## Original description

Returns the specified commit.
