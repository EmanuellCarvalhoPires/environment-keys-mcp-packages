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
path: "/workspaces/{workspace}/pipelines-config/variables/{variable_uuid}"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_delete_a_variable_for_a_workspace]]"
---
# Bitbucket - Delete a variable for a workspace

**Delete a variable for a workspace** — `DELETE /workspaces/{workspace}/pipelines-config/variables/{variable_uuid}`

- Run by the tool [[bitbucket_delete_a_variable_for_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/workspaces/{{service.workspace}}/pipelines-config/variables/{{param:variable_uuid}}
Authorization: {{service.auth_token}}
```

## Parameters

- `variable_uuid` (path, string, required) — The UUID of the variable to delete.

## Original description

Delete a workspace level variable.
