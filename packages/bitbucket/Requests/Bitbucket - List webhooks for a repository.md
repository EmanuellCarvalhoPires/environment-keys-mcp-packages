---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/hooks"
category: "Repositories"
writes_data: false
tool_note: "[[bitbucket_list_webhooks_for_a_repository]]"
---
# Bitbucket - List webhooks for a repository

**List webhooks for a repository** — `GET /repositories/{workspace}/{repo_slug}/hooks`

- Run by the tool [[bitbucket_list_webhooks_for_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/hooks
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.

## Original description

Returns a paginated list of webhooks installed on this repository.
