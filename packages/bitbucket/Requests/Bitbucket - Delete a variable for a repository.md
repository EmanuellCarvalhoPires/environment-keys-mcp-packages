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
path: "/repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid}"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_delete_a_variable_for_a_repository]]"
---
# Bitbucket - Delete a variable for a repository

**Delete a variable for a repository** — `DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid}`

- Run by the tool [[bitbucket_delete_a_variable_for_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines_config/variables/{{param:variable_uuid}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `variable_uuid` (path, string, required) — The UUID of the variable to delete.

## Original description

Delete a repository level variable.
