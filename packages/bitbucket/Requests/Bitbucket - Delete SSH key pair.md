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
path: "/repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_delete_ssh_key_pair]]"
---
# Bitbucket - Delete SSH key pair

**Delete SSH key pair** — `DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair`

- Run by the tool [[bitbucket_delete_ssh_key_pair]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines_config/ssh/key_pair
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.

## Original description

Delete the repository SSH key pair.
