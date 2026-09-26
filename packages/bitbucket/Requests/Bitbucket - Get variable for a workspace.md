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
path: "/workspaces/{workspace}/pipelines-config/variables/{variable_uuid}"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_get_variable_for_a_workspace]]"
---
# Bitbucket - Get variable for a workspace

**Get variable for a workspace** — `GET /workspaces/{workspace}/pipelines-config/variables/{variable_uuid}`

- Run by the tool [[bitbucket_get_variable_for_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/pipelines-config/variables/{{param:variable_uuid}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `variable_uuid` (path, string, required) — The UUID of the variable to retrieve.

## Original description

Retrieve a workspace level variable.
