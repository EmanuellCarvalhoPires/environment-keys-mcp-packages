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
path: "/workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}"
category: "Projects"
writes_data: false
tool_note: "[[bitbucket_get_a_default_reviewer]]"
---
# Bitbucket - Get a default reviewer

**Get a default reviewer** — `GET /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}`

- Run by the tool [[bitbucket_get_a_default_reviewer]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}/default-reviewers/{{param:selected_user}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.
- `selected_user` (path, string, required) — Value of selecteduser in the path.

## Original description

Returns the specified default reviewer.
