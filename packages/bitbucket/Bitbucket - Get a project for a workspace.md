---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/workspaces/{workspace}/projects/{project_key}"
category: "Projects"
writes_data: false
tool_note: "[[bitbucket_get_a_project_for_a_workspace]]"
---
# Bitbucket - Get a project for a workspace

**Get a project for a workspace** — `GET /workspaces/{workspace}/projects/{project_key}`

- Run by the tool [[bitbucket_get_a_project_for_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.

## Original description

Returns the requested project.
