---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}"
category: "Projects"
writes_data: true
tool_note: "[[bitbucket_add_the_specific_user_as_a_default_reviewer_for_the_pr]]"
---
# Bitbucket - Add the specific user as a default reviewer for the project

**Add the specific user as a default reviewer for the project** — `PUT /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}`

- Run by the tool [[bitbucket_add_the_specific_user_as_a_default_reviewer_for_the_pr]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}/default-reviewers/{{param:selected_user}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.
- `selected_user` (path, string, required) — Value of selecteduser in the path.

## Original description

Adds the specified user to the project's list of default reviewers. The method is
idempotent. Accepts an optional body containing the `uuid` of the user to be added.
