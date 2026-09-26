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
path: "/repositories/{workspace}/{repo_slug}/pipelines_config/variables"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_create_a_variable_for_a_repository]]"
---
# Bitbucket - Create a variable for a repository

**Create a variable for a repository** — `POST /repositories/{workspace}/{repo_slug}/pipelines_config/variables`

- Run by the tool [[bitbucket_create_a_variable_for_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines_config/variables
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create a repository level variable.
