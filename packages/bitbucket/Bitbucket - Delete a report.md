---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/reports
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}"
category: "Reports"
writes_data: true
tool_note: "[[bitbucket_delete_a_report]]"
---
# Bitbucket - Delete a report

**Delete a report** — `DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}`

- Run by the tool [[bitbucket_delete_a_report]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commit/{{param:commit}}/reports/{{param:reportId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `commit` (path, string, required) — The commit the report belongs to.
- `reportId` (path, string, required) — Either the uuid or external-id of the report.

## Original description

Deletes a single Report matching the provided ID.
