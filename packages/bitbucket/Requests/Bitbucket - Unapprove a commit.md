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
path: "/repositories/{workspace}/{repo_slug}/commit/{commit}/approve"
category: "Commits"
writes_data: true
tool_note: "[[bitbucket_unapprove_a_commit]]"
---
# Bitbucket - Unapprove a commit

**Unapprove a commit** — `DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/approve`

- Run by the tool [[bitbucket_unapprove_a_commit]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commit/{{param:commit}}/approve
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `commit` (path, string, required) — Value of commit in the path.

## Original description

Redact the authenticated user's approval of the specified commit.

This operation is only available to users that have explicit access to
the repository. In contrast, just the fact that a repository is
publicly accessible to users does not give them the ability to approve
commits.
