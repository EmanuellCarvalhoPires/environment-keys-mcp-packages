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
path: "/workspaces/{workspace}/projects"
category: "Workspaces"
writes_data: false
tool_note: "[[bitbucket_list_projects_in_a_workspace]]"
---
# Bitbucket - List projects in a workspace

**List projects in a workspace** — `GET /workspaces/{workspace}/projects`

- Run by the tool [[bitbucket_list_projects_in_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/projects
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns the list of projects in this workspace.
