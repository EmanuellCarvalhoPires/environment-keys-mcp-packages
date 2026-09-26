---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/pipelines-config/caches/{cache_uuid}/content-uri"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_get_cache_content_uri]]"
---
# Bitbucket - Get cache content URI

**Get cache content URI** — `GET /repositories/{workspace}/{repo_slug}/pipelines-config/caches/{cache_uuid}/content-uri`

- Run by the tool [[bitbucket_get_cache_content_uri]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines-config/caches/{{param:cache_uuid}}/content-uri
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `cache_uuid` (path, string, required) — The UUID of the cache.

## Original description

Retrieve the URI of the content of the specified cache.
