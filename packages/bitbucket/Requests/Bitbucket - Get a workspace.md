---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/workspaces/{workspace}"
category: "Workspaces"
writes_data: false
tool_note: "[[bitbucket_get_a_workspace]]"
---
# Bitbucket - Get a workspace

**Get a workspace** — `GET /workspaces/{workspace}`

- Run by the tool [[bitbucket_get_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns the requested workspace.
