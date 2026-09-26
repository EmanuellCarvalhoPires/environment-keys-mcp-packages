---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/hooks/{uid}"
category: "Repositories"
writes_data: false
tool_note: "[[bitbucket_get_a_webhook_for_a_repository]]"
---
# Bitbucket - Get a webhook for a repository

**Get a webhook for a repository** — `GET /repositories/{workspace}/{repo_slug}/hooks/{uid}`

- Run by the tool [[bitbucket_get_a_webhook_for_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/hooks/{{param:uid}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `uid` (path, string, required) — Value of uid in the path.

## Original description

Returns the webhook with the specified id installed on the specified
repository.
