---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/commits"
category: "Commits"
writes_data: false
tool_note: "[[bitbucket_list_commits]]"
---
# Bitbucket - List commits

**List commits** — `GET /repositories/{workspace}/{repo_slug}/commits`

- Run by the tool [[bitbucket_list_commits]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commits
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.

## Original description

These are the repository's commits. They are paginated and returned
in reverse chronological order, similar to the output of `git log`.
Like these tools, the DAG can be filtered.

#### GET /repositories/{workspace}/{repo_slug}/commits/

Returns all commits in the repo in topological order (newest commit
first). All branches and tags are included (similar to
`git log --all`).

#### GET /repositories/{workspace}/{repo_slug}/commits/?exclude=master

Returns all commits in the repo that are not on master
(similar to `git log --all ^master`).

#### GET /repositories/{workspace}/{repo_slug}/commits/?include=foo&include=bar&exclude=fu&exclude=fubar

Returns all commits that are on refs `foo` or `bar`, but not on `fu` or
`fubar` (similar to `git log foo bar ^fu ^fubar`).

An optional `path` parameter can be specified that will limit the
results to commits that affect that path. `path` can either be a file
or a directory. If a directory is specified, commits are returned that
have modified any file in the directory tree rooted by `path`. It is
important to note that if the `path` parameter is specified, the commits
returned by this endpoint may no longer be a DAG, parent commits that
do not modify the path will be omitted from the response.

#### GET /repositories/{workspace}/{repo_slug}/commits/?path=README.md&include=foo&include=bar&exclude=master

Returns all commits that are on refs `foo` or `bar`, but not on `master`
that changed the file README.md.

#### GET /repositories/{workspace}/{repo_slug}/commits/?path=src/&include=foo&include=bar&exclude=master

Returns all commits that are on refs `foo` or `bar`, but not on `master`
that changed to a file in any file in the directory src or its children.

Because the response could include a very large number of commits, it
is paginated. Follow the 'next' link in the response to navigate to the
next page of commits. As with other paginated resources, do not
construct your own links.

When the include and exclude parameters are more than can fit in a
query string, clients can use a `x-www-form-urlencoded` POST instead.
