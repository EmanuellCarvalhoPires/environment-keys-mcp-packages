---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/commit/{commit}/comments"
category: "Commits"
writes_data: true
tool_note: "[[bitbucket_create_comment_for_a_commit]]"
---
# Bitbucket - Create comment for a commit

**Create comment for a commit** — `POST /repositories/{workspace}/{repo_slug}/commit/{commit}/comments`

- Run by the tool [[bitbucket_create_comment_for_a_commit]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commit/{{param:commit}}/comments
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `commit` (path, string, required) — Value of commit in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates new comment on the specified commit.

To post a reply to an existing comment, include the `parent.id` field:

```
$ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/commit/db9ba1e031d07a02603eae0e559a7adc010257fc/comments/ \
  -X POST -u evzijst \
  -H 'Content-Type: application/json' \
  -d '{"content": {"raw": "One more thing!"},
       "parent": {"id": 5728901} }'
```
