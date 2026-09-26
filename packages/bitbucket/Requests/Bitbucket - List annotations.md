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
path: "/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations"
category: "Reports"
writes_data: false
tool_note: "[[bitbucket_list_annotations]]"
---
# Bitbucket - List annotations

**List annotations** — `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations`

- Run by the tool [[bitbucket_list_annotations]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commit/{{param:commit}}/reports/{{param:reportId}}/annotations
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `commit` (path, string, required) — The commit for which to retrieve reports.
- `reportId` (path, string, required) — Uuid or external-if of the report for which to get annotations for.

## Original description

Returns a paginated list of Annotations for a specified report.
