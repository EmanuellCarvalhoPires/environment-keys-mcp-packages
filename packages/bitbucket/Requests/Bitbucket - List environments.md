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
path: "/repositories/{workspace}/{repo_slug}/environments"
category: "Deployments"
writes_data: false
tool_note: "[[bitbucket_list_environments]]"
---
# Bitbucket - List environments

**List environments** — `GET /repositories/{workspace}/{repo_slug}/environments`

- Run by the tool [[bitbucket_list_environments]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/environments
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.

## Original description

Find environments
