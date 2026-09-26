---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/reports
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/commit/{commit}/reports"
category: "Reports"
writes_data: false
tool_note: "[[bitbucket_list_reports]]"
---
# Bitbucket - List reports

**List reports** — `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports`

- Run by the tool [[bitbucket_list_reports]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commit/{{param:commit}}/reports
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `commit` (path, string, required) — The commit for which to retrieve reports.

## Original description

Returns a paginated list of Reports linked to this commit.
