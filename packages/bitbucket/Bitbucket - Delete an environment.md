---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/repositories/{workspace}/{repo_slug}/environments/{environment_uuid}"
category: "Deployments"
writes_data: true
tool_note: "[[bitbucket_delete_an_environment]]"
---
# Bitbucket - Delete an environment

**Delete an environment** — `DELETE /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}`

- Run by the tool [[bitbucket_delete_an_environment]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/environments/{{param:environment_uuid}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `environment_uuid` (path, string, required) — The environment UUID.

## Original description

Delete an environment
