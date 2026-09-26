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
path: "/repositories/{workspace}/{repo_slug}/branching-model/settings"
category: "Branching model"
writes_data: true
tool_note: "[[bitbucket_update_the_branching_model_config_for_a_repository]]"
---
# Bitbucket - Update the branching model config for a repository

**Update the branching model config for a repository** — `PUT /repositories/{workspace}/{repo_slug}/branching-model/settings`

- Run by the tool [[bitbucket_update_the_branching_model_config_for_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/branching-model/settings
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.

## Original description

Update the branching model configuration for a repository.

The `development` branch can be configured to a specific branch or to
track the main branch. When set to a specific branch it must
currently exist. Only the passed properties will be updated. The
properties not passed will be left unchanged. A request without a
`development` property will leave the development branch unchanged.

It is possible for the `development` branch to be invalid. This
happens when it points at a specific branch that has been
deleted. This is indicated in the `is_valid` field for the branch. It is
not possible to update the settings for `development` if that
would leave the branch in an invalid state. Such a request will be
rejected.

The `production` branch can be a specific branch, the main
branch or disabled. When set to a specific branch it must currently
exist. The `enabled` property can be used to enable (`true`) or
disable (`false`) it. Only the passed properties will be updated. The
properties not passed will be left unchanged. A request without a
`production` property will leave the production branch unchanged.

It is possible for the `production` branch to be invalid. This
happens when it points at a specific branch that has been
deleted. This is indicated in the `is_valid` field for the branch. A
request that would leave `production` enabled and invalid will be
rejected. It is possible to update `production` and make it invalid if
it would also be left disabled.

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

There is currently a side effect when using this API endpoint. If the
repository is inheriting branching model settings from its project,
updating the branching model for this repository will disable the
project setting inheritance.


We have deprecated this side effect and will remove it on 1 August 2022.
