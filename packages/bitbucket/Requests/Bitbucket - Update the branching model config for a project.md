---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branching-model
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/workspaces/{workspace}/projects/{project_key}/branching-model/settings"
category: "Branching model"
writes_data: true
tool_note: "[[bitbucket_update_the_branching_model_config_for_a_project]]"
---
# Bitbucket - Update the branching model config for a project

**Update the branching model config for a project** — `PUT /workspaces/{workspace}/projects/{project_key}/branching-model/settings`

- Run by the tool [[bitbucket_update_the_branching_model_config_for_a_project]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}/branching-model/settings
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.

## Original description

Update the branching model configuration for a project.

The `development` branch can be configured to a specific branch or to
track the main branch. Any branch name can be supplied, but will only
successfully be applied to a repository via inheritance if that branch
exists for that repository. Only the passed properties will be updated. The
properties not passed will be left unchanged. A request without a
`development` property will leave the development branch unchanged.

The `production` branch can be a specific branch, the main
branch or disabled. Any branch name can be supplied, but will only
successfully be applied to a repository via inheritance if that branch
exists for that repository. The `enabled` property can be used to enable (`true`)
or disable (`false`) it. Only the passed properties will be updated. The
properties not passed will be left unchanged. A request without a
`production` property will leave the production branch unchanged.

The `branch_types` property contains the branch types to be updated.
Only the branch types passed will be updated. All updates will be
rejected if it would leave the branching model in an invalid state.
For branch types this means that:

1. The prefixes for all enabled branch types are valid. For example,
   it is not possible to use '*' inside a Git prefix.
2. A prefix of an enabled branch type must not be a prefix of another
   enabled branch type. This is to ensure that a branch can be easily
   classified by its prefix unambiguously.

It is possible to store an invalid prefix if that branch type would be
left disabled. Only the passed properties will be updated. The
properties not passed will be left unchanged. Each branch type must
have a `kind` property to identify it.

The `default_branch_deletion` property is a string. The value of `true`
indicates to delete branches by default. The value of `false` indicates
that branches will not be deleted by default. A request without a
`default_branch_deletion` property will leave it unchanged. Other values
would be ignored.
