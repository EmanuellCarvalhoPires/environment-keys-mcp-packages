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
path: "/workspaces/{workspace}/pipelines-config/variables/{variable_uuid}"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_update_variable_for_a_workspace]]"
---
# Bitbucket - Update variable for a workspace

**Update variable for a workspace** — `PUT /workspaces/{workspace}/pipelines-config/variables/{variable_uuid}`

- Run by the tool [[bitbucket_update_variable_for_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/workspaces/{{service.workspace}}/pipelines-config/variables/{{param:variable_uuid}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `variable_uuid` (path, string, required) — The UUID of the variable.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update a workspace level variable.
