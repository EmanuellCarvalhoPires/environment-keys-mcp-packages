---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/reports
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}"
category: "Reports"
writes_data: false
tool_note: "[[bitbucket_get_a_report]]"
---
# Bitbucket - Get a report

**Get a report** — `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}`

- Run by the tool [[bitbucket_get_a_report]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commit/{{param:commit}}/reports/{{param:reportId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `commit` (path, string, required) — The commit the report belongs to.
- `reportId` (path, string, required) — Either the uuid or external-id of the report.

## Original description

Returns a single Report matching the provided ID.
