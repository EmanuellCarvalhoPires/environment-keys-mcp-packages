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
path: "/repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}"
category: "Deployments"
writes_data: false
tool_note: "[[bitbucket_get_a_repository_deploy_key]]"
---
# Bitbucket - Get a repository deploy key

**Get a repository deploy key** — `GET /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}`

- Run by the tool [[bitbucket_get_a_repository_deploy_key]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/deploy-keys/{{param:key_id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `key_id` (path, string, required) — Value of keyid in the path.

## Original description

Returns the deploy key belonging to a specific key.
