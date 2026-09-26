---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/action
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/forks"
category: "Repositories"
writes_data: true
tool_note: "[[bitbucket_fork_a_repository]]"
---
# Bitbucket - Fork a repository

**Fork a repository** — `POST /repositories/{workspace}/{repo_slug}/forks`

- Run by the tool [[bitbucket_fork_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/forks
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new fork of the specified repository.

#### Forking a repository

To create a fork, specify the workspace explicitly as part of the
request body:

```
$ curl -X POST -u jdoe https://api.bitbucket.org/2.0/repositories/atlassian/bbql/forks \
  -H 'Content-Type: application/json' -d '{
    "name": "bbql_fork",
    "workspace": {
      "slug": "atlassian"
    }
}'
```

To fork a repository into the same workspace, also specify a new `name`.

When you specify a value for `name`, it will also affect the `slug`.
The `slug` is reflected in the repository URL of the new fork. It is
derived from `name` by substituting non-ASCII characters, removes
whitespace, and changes characters to lower case. For example,
`My repo` would turn into `my_repo`.

You need contributor access to create new forks within a workspace.


#### Change the properties of a new fork

By default the fork inherits most of its properties from the parent.
However, since the optional POST body document follows the normal
`repository` JSON schema and you can override the new fork's
properties.

Properties that can be overridden include:

* description
* fork_policy
* language
* mainbranch
* is_private (note that a private repo's fork_policy might prohibit
  the creation of public forks, in which `is_private=False` would fail)
* has_issues (to initialize or disable the new repo's issue tracker --
  note that the actual contents of the parent repository's issue
  tracker are not copied during forking)
* has_wiki (to initialize or disable the new repo's wiki --
  note that the actual contents of the parent repository's wiki are not
  copied during forking)
* project (when forking into a private project, the fork's `is_private`
  must be `true`)

Properties that cannot be modified include:

* scm
* parent
* full_name
