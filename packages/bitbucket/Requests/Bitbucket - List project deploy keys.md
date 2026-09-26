---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/workspaces/{workspace}/projects/{project_key}/deploy-keys"
category: "Deployments"
writes_data: false
tool_note: "[[bitbucket_list_project_deploy_keys]]"
---
# Bitbucket - List project deploy keys

**List project deploy keys** — `GET /workspaces/{workspace}/projects/{project_key}/deploy-keys`

- Run by the tool [[bitbucket_list_project_deploy_keys]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}/deploy-keys
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.

## Original description

Returns all deploy keys belonging to a project.
