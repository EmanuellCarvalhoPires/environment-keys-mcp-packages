---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/workspaces/{workspace}/pipelines-config/variables"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_list_variables_for_a_workspace]]"
---
# Bitbucket - List variables for a workspace

**List variables for a workspace** — `GET /workspaces/{workspace}/pipelines-config/variables`

- Run by the tool [[bitbucket_list_variables_for_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/pipelines-config/variables
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Find workspace level variables.
