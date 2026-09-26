---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/search
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/commits/{revision}"
category: "Commits"
writes_data: false
tool_note: "[[bitbucket_list_commits_for_revision_using_include_exclude]]"
---
# Bitbucket - List commits for revision using include exclude

**List commits for revision using include/exclude** — `POST /repositories/{workspace}/{repo_slug}/commits/{revision}`

- Run by the tool [[bitbucket_list_commits_for_revision_using_include_exclude]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commits/{{param:revision}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `revision` (path, string, required) — Value of revision in the path.

## Original description

Identical to `GET /repositories/{workspace}/{repo_slug}/commits/{revision}`,
except that POST allows clients to place the include and exclude
parameters in the request body to avoid URL length issues.

**Note that this resource does NOT support new commit creation.**
