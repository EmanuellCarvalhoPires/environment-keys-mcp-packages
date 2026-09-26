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
path: "/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid}"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_delete_a_variable_for_an_environment]]"
---
# Bitbucket - Delete a variable for an environment

**Delete a variable for an environment** — `DELETE /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid}`

- Run by the tool [[bitbucket_delete_a_variable_for_an_environment]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/deployments_config/environments/{{param:environment_uuid}}/variables/{{param:variable_uuid}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `environment_uuid` (path, string, required) — The environment.
- `variable_uuid` (path, string, required) — The UUID of the variable to delete.

## Original description

Delete a deployment environment level variable.
