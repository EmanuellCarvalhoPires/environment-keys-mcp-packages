---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/downloads
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/repositories/{workspace}/{repo_slug}/downloads/{filename}"
category: "Downloads"
writes_data: true
tool_note: "[[bitbucket_delete_a_download_artifact]]"
---
# Bitbucket - Delete a download artifact

**Delete a download artifact** — `DELETE /repositories/{workspace}/{repo_slug}/downloads/{filename}`

- Run by the tool [[bitbucket_delete_a_download_artifact]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/downloads/{{param:filename}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `filename` (path, string, required) — Value of filename in the path.

## Original description

Deletes the specified download artifact from the repository.
