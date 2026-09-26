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
path: "/repositories/{workspace}/{repo_slug}/diff/{spec}"
category: "Commits"
writes_data: false
tool_note: "[[bitbucket_compare_two_commits]]"
---
# Bitbucket - Compare two commits

**Compare two commits** — `GET /repositories/{workspace}/{repo_slug}/diff/{spec}`

- Run by the tool [[bitbucket_compare_two_commits]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/diff/{{param:spec}}?context={{param:context}}&path={{param:path}}&ignore_whitespace={{param:ignore_whitespace}}&binary={{param:binary}}&renames={{param:renames}}&merge={{param:merge}}&topic={{param:topic}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `spec` (path, string, required) — Value of spec in the path.
- `context` (query, string, optional) — Generate diffs with lines of context instead of the usual three.
- `path` (query, string, optional) — Limit the diff to a particular file (this parameter can be repeated for multiple paths).
- `ignore_whitespace` (query, string, optional) — Generate diffs that ignore whitespace.
- `binary` (query, string, optional) — Generate diffs that include binary files, true if omitted.
- `renames` (query, string, optional) — Whether to perform rename detection, true if omitted.
- `merge` (query, string, optional) — This parameter is deprecated. The 'topic' parameter should be used instead. The 'merge' and 'topic' parameters cannot be both used at the same time.
- `topic` (query, string, optional) — If true, returns 2-way 'three-dot' diff. This is a diff between the source commit and the merge base of the source commit and the destination commit.

## Original description

Produces a raw git-style diff.

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

#### Comparison to patches

While similar to patches, diffs:

* Don't have a commit header (username, commit message, etc)
* Support the optional `path=foo/bar.py` query param to filter
  the diff to just that one file diff

#### Response

The raw diff is returned as-is, in whatever encoding the files in the
repository use. It is not decoded into unicode. As such, the
content-type is `text/plain`.
