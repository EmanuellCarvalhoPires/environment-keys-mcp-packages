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
path: "/repositories/{workspace}/{repo_slug}/branching-model/settings"
category: "Branching model"
writes_data: false
tool_note: "[[bitbucket_get_the_branching_model_config_for_a_repository]]"
---
# Bitbucket - Get the branching model config for a repository

**Get the branching model config for a repository** — `GET /repositories/{workspace}/{repo_slug}/branching-model/settings`

- Run by the tool [[bitbucket_get_the_branching_model_config_for_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/branching-model/settings
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.

## Original description

Return the branching model configuration for a repository. The returned
object:

1. Always has a `development` property for the development branch.
2. Always a `production` property for the production branch. The
   production branch can be disabled.
3. The `branch_types` contains all the branch types.
4. `default_branch_deletion` indicates whether branches will be
    deleted by default on merge.

This is the raw configuration for the branching model. A client
wishing to see the branching model with its actual current branches may
find the [active model API](/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-workspace-repo-slug-branching-model-get) more useful.
