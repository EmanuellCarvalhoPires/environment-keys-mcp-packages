---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/diffstat/{spec}"
category: "Commits"
writes_data: false
tool_note: "[[bitbucket_compare_two_commit_diff_stats]]"
---
# Bitbucket - Compare two commit diff stats

**Compare two commit diff stats** — `GET /repositories/{workspace}/{repo_slug}/diffstat/{spec}`

- Run by the tool [[bitbucket_compare_two_commit_diff_stats]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/diffstat/{{param:spec}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `spec` (path, string, required) — Value of spec in the path.

## Original description

Produces a response in JSON format with a record for every path
modified, including information on the type of the change and the
number of lines added and removed.

#### Single commit spec

If the `spec` argument to this API is a single commit, the diff is
produced against the first parent of the specified commit.

#### Two commit spec

Two commits separated by `..` may be provided as the `spec`, e.g.,
`3a8b42..9ff173`. When two commits are provided and the `topic` query
parameter is true, this API produces a 2-way three dot diff.
This is the diff between source commit and the merge base of the source
commit and the destination commit. When the `topic` query param is false,
a simple git-style diff is produced.

The two commits are interpreted as follows:

* First commit: the commit containing the changes we wish to preview
* Second commit: the commit representing the state to which we want to
  compare the first commit
* **Note**: This is the opposite of the order used in `git diff`.
