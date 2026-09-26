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
path: "/workspaces/{workspace}/projects/{project_key}/branching-model/settings"
category: "Branching model"
writes_data: false
tool_note: "[[bitbucket_get_the_branching_model_config_for_a_project]]"
---
# Bitbucket - Get the branching model config for a project

**Get the branching model config for a project** — `GET /workspaces/{workspace}/projects/{project_key}/branching-model/settings`

- Run by the tool [[bitbucket_get_the_branching_model_config_for_a_project]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}/branching-model/settings
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.

## Original description

Return the branching model configuration for a project. The returned
object:

1. Always has a `development` property for the development branch.
2. Always a `production` property for the production branch. The
   production branch can be disabled.
3. The `branch_types` contains all the branch types.
4. `default_branch_deletion` indicates whether branches will be
    deleted by default on merge.


This is the raw configuration for the branching model. A client
wishing to see the branching model with its actual current branches may find the
[active model API](#api-workspaces-workspace-projects-project-key-branching-model-get)
more useful.
