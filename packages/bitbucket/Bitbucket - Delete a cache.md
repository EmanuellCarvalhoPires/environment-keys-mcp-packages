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
path: "/repositories/{workspace}/{repo_slug}/pipelines-config/caches/{cache_uuid}"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_delete_a_cache]]"
---
# Bitbucket - Delete a cache

**Delete a cache** — `DELETE /repositories/{workspace}/{repo_slug}/pipelines-config/caches/{cache_uuid}`

- Run by the tool [[bitbucket_delete_a_cache]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines-config/caches/{{param:cache_uuid}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `cache_uuid` (path, string, required) — The UUID of the cache to delete.

## Original description

Delete a repository cache.
