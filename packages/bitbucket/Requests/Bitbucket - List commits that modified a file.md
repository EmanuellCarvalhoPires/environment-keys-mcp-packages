---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/source
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/filehistory/{commit}/{path}"
category: "Source"
writes_data: false
tool_note: "[[bitbucket_list_commits_that_modified_a_file]]"
---
# Bitbucket - List commits that modified a file

**List commits that modified a file** — `GET /repositories/{workspace}/{repo_slug}/filehistory/{commit}/{path}`

- Run by the tool [[bitbucket_list_commits_that_modified_a_file]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/filehistory/{{param:commit}}/{{param:path}}?renames={{param:renames}}&q={{param:q}}&sort={{param:sort}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `commit` (path, string, required) — Value of commit in the path.
- `path` (path, string, required) — Value of path in the path.
- `renames` (query, string, optional) — When true, Bitbucket will follow the history of the file across renames (this is the default behavior). This can be turned off by specifying false.
- `q` (query, string, optional) — Query string to narrow down the response as per filtering and sorting.
- `sort` (query, string, optional) — Name of a response property sort the result by as per filtering and sorting.

## Original description

Returns a paginated list of commits that modified the specified file.

Commits are returned in reverse chronological order. This is roughly
equivalent to the following commands:

    $ git log --follow --date-order  

By default, Bitbucket will follow renames and the path name in the
returned entries reflects that. This can be turned off using the
`?renames=false` query parameter.

Results are returned in descending chronological order by default, and
like most endpoints you can
[filter and sort](/cloud/bitbucket/rest/intro/#filtering) the response to
only provide exactly the data you want.

The example response returns commits made before 2011-05-18 against a file
named `README.rst`. The results are filtered to only return the path and
date. This request can be made using:

```
$ curl 'https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/filehistory/master/README.rst'\
  '?fields=values.next,values.path,values.commit.date&q=commit.date<=2011-05-18'
```

In the response you can see that the file was renamed to `README.rst`
by the commit made on 2011-05-16, and was previously named `README.txt`.
