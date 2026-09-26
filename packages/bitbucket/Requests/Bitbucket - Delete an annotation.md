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
path: "/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}"
category: "Reports"
writes_data: true
tool_note: "[[bitbucket_delete_an_annotation]]"
---
# Bitbucket - Delete an annotation

**Delete an annotation** — `DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}`

- Run by the tool [[bitbucket_delete_an_annotation]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commit/{{param:commit}}/reports/{{param:reportId}}/annotations/{{param:annotationId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `commit` (path, string, required) — The commit the annotation belongs to.
- `reportId` (path, string, required) — Either the uuid or external-id of the annotation.
- `annotationId` (path, string, required) — Either the uuid or external-id of the annotation.

## Original description

Deletes a single Annotation matching the provided ID.
