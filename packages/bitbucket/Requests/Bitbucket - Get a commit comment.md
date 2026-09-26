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
path: "/repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}"
category: "Commits"
writes_data: false
tool_note: "[[bitbucket_get_a_commit_comment]]"
---
# Bitbucket - Get a commit comment

**Get a commit comment** — `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}`

- Run by the tool [[bitbucket_get_a_commit_comment]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commit/{{param:commit}}/comments/{{param:comment_id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `commit` (path, string, required) — Value of commit in the path.
- `comment_id` (path, string, required) — Value of commentid in the path.

## Original description

Returns the specified commit comment.
