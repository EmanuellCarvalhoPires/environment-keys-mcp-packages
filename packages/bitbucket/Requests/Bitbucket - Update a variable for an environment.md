---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid}"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_update_a_variable_for_an_environment]]"
---
# Bitbucket - Update a variable for an environment

**Update a variable for an environment** — `PUT /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid}`

- Run by the tool [[bitbucket_update_a_variable_for_an_environment]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/deployments_config/environments/{{param:environment_uuid}}/variables/{{param:variable_uuid}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `environment_uuid` (path, string, required) — The environment.
- `variable_uuid` (path, string, required) — The UUID of the variable to update.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update a deployment environment level variable.
