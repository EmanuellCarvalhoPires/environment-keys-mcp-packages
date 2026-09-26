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
path: "/repositories/{workspace}/{repo_slug}/deployments/{deployment_uuid}"
category: "Deployments"
writes_data: false
tool_note: "[[bitbucket_get_a_deployment]]"
---
# Bitbucket - Get a deployment

**Get a deployment** — `GET /repositories/{workspace}/{repo_slug}/deployments/{deployment_uuid}`

- Run by the tool [[bitbucket_get_a_deployment]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/deployments/{{param:deployment_uuid}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `deployment_uuid` (path, string, required) — The deployment UUID.

## Original description

Retrieve a deployment
