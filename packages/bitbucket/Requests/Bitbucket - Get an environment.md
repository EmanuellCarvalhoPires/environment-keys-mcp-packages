---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/environments/{environment_uuid}"
category: "Deployments"
writes_data: false
tool_note: "[[bitbucket_get_an_environment]]"
---
# Bitbucket - Get an environment

**Get an environment** — `GET /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}`

- Run by the tool [[bitbucket_get_an_environment]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/environments/{{param:environment_uuid}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `environment_uuid` (path, string, required) — The environment UUID.

## Original description

Retrieve an environment
