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
path: "/workspaces/{workspace}/projects/{project_key}/deploy-keys/{key_id}"
category: "Deployments"
writes_data: false
tool_note: "[[bitbucket_get_a_project_deploy_key]]"
---
# Bitbucket - Get a project deploy key

**Get a project deploy key** — `GET /workspaces/{workspace}/projects/{project_key}/deploy-keys/{key_id}`

- Run by the tool [[bitbucket_get_a_project_deploy_key]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}/deploy-keys/{{param:key_id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.
- `key_id` (path, string, required) — Value of keyid in the path.

## Original description

Returns the deploy key belonging to a specific key ID.
