---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commit-statuses
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build/{key}"
category: "Commit statuses"
writes_data: true
tool_note: "[[bitbucket_update_a_build_status_for_a_commit]]"
---
# Bitbucket - Update a build status for a commit

**Update a build status for a commit** — `PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build/{key}`

- Run by the tool [[bitbucket_update_a_build_status_for_a_commit]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commit/{{param:commit}}/statuses/build/{{param:key}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `commit` (path, string, required) — Value of commit in the path.
- `key` (path, string, required) — Value of key in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Used to update the current status of a build status object on the
specific commit.

This operation can also be used to change other properties of the
build status:

* `state`
* `name`
* `description`
* `url`
* `refname`

The `key` cannot be changed.
