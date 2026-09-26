---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_create_a_variable_for_an_environment]]"
---
# Bitbucket - Create a variable for an environment

**Create a variable for an environment** — `POST /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables`

- Run by the tool [[bitbucket_create_a_variable_for_an_environment]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/deployments_config/environments/{{param:environment_uuid}}/variables
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `environment_uuid` (path, string, required) — The environment.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create a deployment environment level variable.
