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
path: "/repositories/{workspace}/{repo_slug}/override-settings"
category: "Repositories"
writes_data: false
tool_note: "[[bitbucket_retrieve_the_inheritance_state_for_repository_settings]]"
---
# Bitbucket - Retrieve the inheritance state for repository settings

**Retrieve the inheritance state for repository settings** — `GET /repositories/{workspace}/{repo_slug}/override-settings`

- Run by the tool [[bitbucket_retrieve_the_inheritance_state_for_repository_settings]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/override-settings
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.

