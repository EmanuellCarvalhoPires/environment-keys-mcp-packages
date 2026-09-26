---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}"
category: "Projects"
writes_data: true
tool_note: "[[bitbucket_remove_the_specific_user_from_the_project_s_default_re]]"
---
# Bitbucket - Remove the specific user from the project's default reviewers

**Remove the specific user from the project's default reviewers** — `DELETE /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}`

- Run by the tool [[bitbucket_remove_the_specific_user_from_the_project_s_default_re]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}/default-reviewers/{{param:selected_user}}
Authorization: {{service.auth_token}}
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.
- `selected_user` (path, string, required) — Value of selecteduser in the path.

## Original description

Removes a default reviewer from the project.

Example:
```
$ curl https://api.bitbucket.org/2.0/.../default-reviewers/%7Bf0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6%7D

HTTP/1.1 204
```
