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
path: "/repositories/{workspace}/{repo_slug}/pipelines-config/caches"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_list_caches]]"
---
# Bitbucket - List caches

**List caches** — `GET /repositories/{workspace}/{repo_slug}/pipelines-config/caches`

- Run by the tool [[bitbucket_list_caches]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines-config/caches
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.

## Original description

Retrieve the repository pipelines caches.
