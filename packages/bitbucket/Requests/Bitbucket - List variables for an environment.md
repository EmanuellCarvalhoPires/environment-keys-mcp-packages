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
path: "/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_list_variables_for_an_environment]]"
---
# Bitbucket - List variables for an environment

**List variables for an environment** — `GET /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables`

- Run by the tool [[bitbucket_list_variables_for_an_environment]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/deployments_config/environments/{{param:environment_uuid}}/variables
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `environment_uuid` (path, string, required) — The environment.

## Original description

Find deployment environment level variables.
