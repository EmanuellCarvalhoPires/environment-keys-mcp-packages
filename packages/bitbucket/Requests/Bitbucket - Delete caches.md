---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/repositories/{workspace}/{repo_slug}/pipelines-config/caches"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_delete_caches]]"
---
# Bitbucket - Delete caches

**Delete caches** — `DELETE /repositories/{workspace}/{repo_slug}/pipelines-config/caches`

- Run by the tool [[bitbucket_delete_caches]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines-config/caches?name={{param:name}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `name` (query, string, required) — The cache name.

## Original description

Delete repository cache versions by name.
