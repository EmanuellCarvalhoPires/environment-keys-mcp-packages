---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/environments"
category: "Deployments"
writes_data: true
tool_note: "[[bitbucket_create_an_environment]]"
---
# Bitbucket - Create an environment

**Create an environment** — `POST /repositories/{workspace}/{repo_slug}/environments`

- Run by the tool [[bitbucket_create_an_environment]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/environments
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create an environment.
