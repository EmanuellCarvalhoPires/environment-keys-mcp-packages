---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branching-model
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/workspaces/{workspace}/projects/{project_key}/branching-model"
category: "Branching model"
writes_data: false
tool_note: "[[bitbucket_get_the_branching_model_for_a_project]]"
---
# Bitbucket - Get the branching model for a project

**Get the branching model for a project** — `GET /workspaces/{workspace}/projects/{project_key}/branching-model`

- Run by the tool [[bitbucket_get_the_branching_model_for_a_project]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}/branching-model
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.

## Original description

Return the branching model set at the project level. This view is
read-only. The branching model settings can be changed using the
[settings](#api-workspaces-workspace-projects-project-key-branching-model-settings-get)
API.

The returned object:

1. Always has a `development` property. `development.name` is
   the user-specified branch that can be inherited by an individual repository's
   branching model.
2. Might have a `production` property. `production` will not
   be present when `production` is disabled.
   `production.name` is the user-specified branch that can be
   inherited by an individual repository's branching model.
3. Always has a `branch_types` array which contains all enabled branch
   types.
