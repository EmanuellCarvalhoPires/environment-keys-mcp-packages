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
path: "/repositories/{workspace}/{repo_slug}/refs/tags"
category: "Refs"
writes_data: false
tool_note: "[[bitbucket_list_tags]]"
---
# Bitbucket - List tags

**List tags** — `GET /repositories/{workspace}/{repo_slug}/refs/tags`

- Run by the tool [[bitbucket_list_tags]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/refs/tags?q={{param:q}}&sort={{param:sort}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `q` (query, string, optional) — Query string to narrow down the response as per filtering and sorting.
- `sort` (query, string, optional) — Field by which the results should be sorted as per filtering and sorting. The name field is handled specially for tags in that, if specified as the sort field, it uses a natural sort order instead of…

## Original description

Returns the tags in the repository.

By default, results will be in the order the underlying source control system returns them and identical to
the ordering one sees when running "$ git tag --list". Note that this follows simple
lexical ordering of the ref names.

This can be undesirable as it does apply any natural sorting semantics, meaning for instance that tags are
sorted ["v10", "v11", "v9"] instead of ["v9", "v10", "v11"].

Sorting can be changed using the ?sort= query parameter. When using ?sort=name to explicitly sort on ref name,
Bitbucket will apply natural sorting and interpret numerical values as numbers instead of strings.
