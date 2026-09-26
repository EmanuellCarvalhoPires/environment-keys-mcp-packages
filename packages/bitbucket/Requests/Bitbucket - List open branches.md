---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/refs
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/refs/branches"
category: "Refs"
writes_data: false
tool_note: "[[bitbucket_list_open_branches]]"
---
# Bitbucket - List open branches

**List open branches** — `GET /repositories/{workspace}/{repo_slug}/refs/branches`

- Run by the tool [[bitbucket_list_open_branches]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/refs/branches?q={{param:q}}&sort={{param:sort}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `q` (query, string, optional) — Query string to narrow down the response as per filtering and sorting.
- `sort` (query, string, optional) — Field by which the results should be sorted as per filtering and sorting. The name field is handled specially for branches in that, if specified as the sort field, it uses a natural sort order instead…

## Original description

Returns a list of all open branches within the specified repository.
Results will be in the order the source control manager returns them.

Branches support [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering)
that can be used to search for specific branches. For instance, to find
all branches that have "stab" in their name:

```
curl -s https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches -G --data-urlencode 'q=name ~ "stab"'
```

By default, results will be in the order the underlying source control system returns them and identical to
the ordering one sees when running "$ git branch --list". Note that this follows simple
lexical ordering of the ref names.

This can be undesirable as it does apply any natural sorting semantics, meaning for instance that tags are
sorted ["v10", "v11", "v9"] instead of ["v9", "v10", "v11"].

Sorting can be changed using the ?q= query parameter. When using ?q=name to explicitly sort on ref name,
Bitbucket will apply natural sorting and interpret numerical values as numbers instead of strings.
