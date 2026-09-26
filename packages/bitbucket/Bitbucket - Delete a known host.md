---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_delete_a_known_host]]"
---
# Bitbucket - Delete a known host

**Delete a known host** — `DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}`

- Run by the tool [[bitbucket_delete_a_known_host]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines_config/ssh/known_hosts/{{param:known_host_uuid}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `known_host_uuid` (path, string, required) — The UUID of the known host to delete.

## Original description

Delete a repository level known host.
