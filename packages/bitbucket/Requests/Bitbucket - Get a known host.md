---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_get_a_known_host]]"
---
# Bitbucket - Get a known host

**Get a known host** — `GET /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}`

- Run by the tool [[bitbucket_get_a_known_host]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines_config/ssh/known_hosts/{{param:known_host_uuid}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `known_host_uuid` (path, string, required) — The UUID of the known host to retrieve.

## Original description

Retrieve a repository level known host.
