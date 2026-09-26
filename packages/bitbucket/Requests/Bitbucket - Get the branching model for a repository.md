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
path: "/repositories/{workspace}/{repo_slug}/branching-model"
category: "Branching model"
writes_data: false
tool_note: "[[bitbucket_get_the_branching_model_for_a_repository]]"
---
# Bitbucket - Get the branching model for a repository

**Get the branching model for a repository** — `GET /repositories/{workspace}/{repo_slug}/branching-model`

- Run by the tool [[bitbucket_get_the_branching_model_for_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/branching-model
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.

## Original description

Return the branching model as applied to the repository. This view is
read-only. The branching model settings can be changed using the
[settings](#api-repositories-workspace-repo-slug-branching-model-settings-get) API.

The returned object:

1. Always has a `development` property. `development.branch` contains
   the actual repository branch object that is considered to be the
   `development` branch. `development.branch` will not be present
   if it does not exist.
2. Might have a `production` property. `production` will not
   be present when `production` is disabled.
   `production.branch` contains the actual branch object that is
   considered to be the `production` branch. `production.branch` will
   not be present if it does not exist.
3. Always has a `branch_types` array which contains all enabled branch
   types.
