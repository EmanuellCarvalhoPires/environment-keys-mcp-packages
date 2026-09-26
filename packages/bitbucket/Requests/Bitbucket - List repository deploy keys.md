---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/deploy-keys"
category: "Deployments"
writes_data: false
tool_note: "[[bitbucket_list_repository_deploy_keys]]"
---
# Bitbucket - List repository deploy keys

**List repository deploy keys** — `GET /repositories/{workspace}/{repo_slug}/deploy-keys`

- Run by the tool [[bitbucket_list_repository_deploy_keys]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/deploy-keys
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.

## Original description

Returns all deploy-keys belonging to a repository.
