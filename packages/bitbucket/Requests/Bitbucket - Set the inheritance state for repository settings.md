---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/repositories/{workspace}/{repo_slug}/override-settings"
category: "Repositories"
writes_data: true
tool_note: "[[bitbucket_set_the_inheritance_state_for_repository_settings]]"
---
# Bitbucket - Set the inheritance state for repository settings

**Set the inheritance state for repository settings** — `PUT /repositories/{workspace}/{repo_slug}/override-settings`

- Run by the tool [[bitbucket_set_the_inheritance_state_for_repository_settings]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/override-settings
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.

