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
path: "/workspaces/{workspace}/projects/{project_key}/deploy-keys/{key_id}"
category: "Deployments"
writes_data: true
tool_note: "[[bitbucket_delete_a_deploy_key_from_a_project]]"
---
# Bitbucket - Delete a deploy key from a project

**Delete a deploy key from a project** — `DELETE /workspaces/{workspace}/projects/{project_key}/deploy-keys/{key_id}`

- Run by the tool [[bitbucket_delete_a_deploy_key_from_a_project]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}/deploy-keys/{{param:key_id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.
- `key_id` (path, string, required) — Value of keyid in the path.

## Original description

This deletes a deploy key from a project.
