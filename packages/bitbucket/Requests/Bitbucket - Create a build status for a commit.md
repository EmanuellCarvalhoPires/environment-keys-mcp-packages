---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commit-statuses
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build"
category: "Commit statuses"
writes_data: true
tool_note: "[[bitbucket_create_a_build_status_for_a_commit]]"
---
# Bitbucket - Create a build status for a commit

**Create a build status for a commit** — `POST /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build`

- Run by the tool [[bitbucket_create_a_build_status_for_a_commit]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commit/{{param:commit}}/statuses/build
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `commit` (path, string, required) — Value of commit in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new build status against the specified commit.

If the specified key already exists, the existing status object will
be overwritten.

Example:

```
curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-repo/commit/e10dae226959c2194f2b07b077c07762d93821cf/statuses/build/           -X POST -u jdoe -H 'Content-Type: application/json'           -d '{
    "key": "MY-BUILD",
    "state": "SUCCESSFUL",
    "description": "42 tests passed",
    "url": "https://www.example.org/my-build-result"
  }'
```

When creating a new commit status, you can use a URI template for the URL.
Templates are URLs that contain variable names that Bitbucket will
evaluate at runtime whenever the URL is displayed anywhere similar to
parameter substitution in
[Bitbucket Connect](https://developer.atlassian.com/bitbucket/concepts/context-parameters.html).
For example, one could use `https://foo.com/builds/{repository.full_name}`
which Bitbucket will turn into `https://foo.com/builds/foo/bar` at render time.
The context variables available are `repository` and `commit`.

To associate a commit status to a pull request, the refname field must be set to the source branch
of the pull request.

Example:
```
curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-repo/commit/e10dae226959c2194f2b07b077c07762d93821cf/statuses/build/           -X POST -u jdoe -H 'Content-Type: application/json'           -d '{
    "key": "MY-BUILD",
    "state": "SUCCESSFUL",
    "description": "42 tests passed",
    "url": "https://www.example.org/my-build-result",
    "refname": "my-pr-branch"
  }'
```
