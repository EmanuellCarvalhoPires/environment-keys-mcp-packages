---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}"
category: "Commits"
writes_data: true
tool_note: "[[bitbucket_delete_a_commit_comment]]"
---
# Bitbucket - Delete a commit comment

**Delete a commit comment** — `DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}`

- Run by the tool [[bitbucket_delete_a_commit_comment]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commit/{{param:commit}}/comments/{{param:comment_id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `commit` (path, string, required) — Value of commit in the path.
- `comment_id` (path, string, required) — Value of commentid in the path.

## Original description

Deletes the specified commit comment.

Note that deleting comments that have visible replies that point to
them will not really delete the resource. This is to retain the integrity
of the original comment tree. Instead, the `deleted` element is set to
`true` and the content is blanked out. The comment will continue to be
returned by the collections and self endpoints.
