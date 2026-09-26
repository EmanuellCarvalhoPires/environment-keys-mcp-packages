---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/snippets/{workspace}/{encoded_id}/{revision}/diff"
category: "Snippets"
writes_data: false
tool_note: "[[bitbucket_get_snippet_changes_between_versions]]"
---
# Bitbucket - Get snippet changes between versions

**Get snippet changes between versions** — `GET /snippets/{workspace}/{encoded_id}/{revision}/diff`

- Run by the tool [[bitbucket_get_snippet_changes_between_versions]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}/{{param:revision}}/diff?path={{param:path}}
Authorization: {{service.auth_token}}
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.
- `revision` (path, string, required) — Value of revision in the path.
- `path` (query, string, optional) — When used, only one the diff of the specified file will be returned.

## Original description

Returns the diff of the specified commit against its first parent.

Note that this resource is different in functionality from the `patch`
resource.

The differences between a diff and a patch are:

* patches have a commit header with the username, message, etc
* diffs support the optional `path=foo/bar.py` query param to filter the
  diff to just that one file diff (not supported for patches)
* for a merge, the diff will show the diff between the merge commit and
  its first parent (identical to how PRs work), while patch returns a
  response containing separate patches for each commit on the second
  parent's ancestry, up to the oldest common ancestor (identical to
  its reachability).

Note that the character encoding of the contents of the diff is
unspecified as Git does not track this, making it hard for
Bitbucket to reliably determine this.
