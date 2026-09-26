---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}"
category: "Deployments"
writes_data: true
tool_note: "[[bitbucket_delete_a_repository_deploy_key]]"
---
# Bitbucket - Delete a repository deploy key

**Delete a repository deploy key** — `DELETE /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}`

- Run by the tool [[bitbucket_delete_a_repository_deploy_key]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/deploy-keys/{{param:key_id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `key_id` (path, string, required) — Value of keyid in the path.

## Original description

This deletes a deploy key from a repository.
