---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_update_a_known_host]]"
---
# Bitbucket - Update a known host

**Update a known host** — `PUT /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}`

- Run by the tool [[bitbucket_update_a_known_host]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines_config/ssh/known_hosts/{{param:known_host_uuid}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `known_host_uuid` (path, string, required) — The UUID of the known host to update.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update a repository level known host.
