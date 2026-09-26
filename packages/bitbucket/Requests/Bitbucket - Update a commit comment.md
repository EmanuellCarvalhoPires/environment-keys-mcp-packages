---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}"
category: "Commits"
writes_data: true
tool_note: "[[bitbucket_update_a_commit_comment]]"
---
# Bitbucket - Update a commit comment

**Update a commit comment** — `PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}`

- Run by the tool [[bitbucket_update_a_commit_comment]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commit/{{param:commit}}/comments/{{param:comment_id}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `commit` (path, string, required) — Value of commit in the path.
- `comment_id` (path, string, required) — Value of commentid in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Used to update the contents of a comment. Only the content of the comment can be updated.

```
$ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/commit/7f71b5/comments/5728901 \
  -X PUT -u evzijst \
  -H 'Content-Type: application/json' \
  -d '{"content": {"raw": "One more thing!"}'
```
