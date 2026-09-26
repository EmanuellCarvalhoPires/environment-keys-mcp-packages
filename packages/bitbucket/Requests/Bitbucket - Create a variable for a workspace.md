---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/workspaces/{workspace}/pipelines-config/variables"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_create_a_variable_for_a_workspace]]"
---
# Bitbucket - Create a variable for a workspace

**Create a variable for a workspace** — `POST /workspaces/{workspace}/pipelines-config/variables`

- Run by the tool [[bitbucket_create_a_variable_for_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/workspaces/{{service.workspace}}/pipelines-config/variables
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create a workspace level variable.
