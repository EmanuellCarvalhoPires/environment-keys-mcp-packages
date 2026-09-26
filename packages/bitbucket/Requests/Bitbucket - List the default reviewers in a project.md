---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/workspaces/{workspace}/projects/{project_key}/default-reviewers"
category: "Projects"
writes_data: false
tool_note: "[[bitbucket_list_the_default_reviewers_in_a_project]]"
---
# Bitbucket - List the default reviewers in a project

**List the default reviewers in a project** — `GET /workspaces/{workspace}/projects/{project_key}/default-reviewers`

- Run by the tool [[bitbucket_list_the_default_reviewers_in_a_project]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}/default-reviewers
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.

## Original description

Return a list of all default reviewers for a project. This is a list of users that will be added as default
reviewers to pull requests for any repository within the project.
