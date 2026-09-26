---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/repositories/{workspace}/{repo_slug}"
category: "Repositories"
writes_data: true
tool_note: "[[bitbucket_update_a_repository]]"
---
# Bitbucket - Update a repository

**Update a repository** — `PUT /repositories/{workspace}/{repo_slug}`

- Run by the tool [[bitbucket_update_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Since this endpoint can be used to both update and to create a
repository, the request body depends on the intent.

#### Creation

See the POST documentation for the repository endpoint for an example
of the request body.

#### Update

Note: Changing the `name` of the repository will cause the location to
be changed. This is because the URL of the repo is derived from the
name (a process called slugification). In such a scenario, it is
possible for the request to fail if the newly created slug conflicts
with an existing repository's slug. But if there is no conflict,
the new location will be returned in the `Location` header of the
response.
