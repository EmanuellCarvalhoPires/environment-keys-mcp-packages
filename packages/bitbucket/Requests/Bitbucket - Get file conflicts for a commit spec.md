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
path: "/repositories/{workspace}/{repo_slug}/file-conflicts/{spec}"
category: "Commits"
writes_data: false
tool_note: "[[bitbucket_get_file_conflicts_for_a_commit_spec]]"
---
# Bitbucket - Get file conflicts for a commit spec

**Get file conflicts for a commit spec** — `GET /repositories/{workspace}/{repo_slug}/file-conflicts/{spec}`

- Run by the tool [[bitbucket_get_file_conflicts_for_a_commit_spec]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/file-conflicts/{{param:spec}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `spec` (path, string, required) — Value of spec in the path.

## Original description

Get file conflicts for a commit spec
