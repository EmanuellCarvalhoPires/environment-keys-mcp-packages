---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/action
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes"
category: "Deployments"
writes_data: true
tool_note: "[[bitbucket_update_an_environment]]"
---
# Bitbucket - Update an environment

**Update an environment** — `POST /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes`

- Run by the tool [[bitbucket_update_an_environment]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/environments/{{param:environment_uuid}}/changes
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `environment_uuid` (path, string, required) — The environment UUID.

## Original description

Update an environment
