---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/source
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/src"
category: "Source"
writes_data: false
tool_note: "[[bitbucket_get_the_root_directory_of_the_main_branch]]"
---
# Bitbucket - Get the root directory of the main branch

**Get the root directory of the main branch** — `GET /repositories/{workspace}/{repo_slug}/src`

- Run by the tool [[bitbucket_get_the_root_directory_of_the_main_branch]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/src?format={{param:format}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `format` (query, string, optional) — Instead of returning the file's contents, return the (json) meta data for it.

## Original description

This endpoint redirects the client to the directory listing of the
root directory on the main branch.

This is equivalent to directly hitting
[/2.0/repositories/{username}/{repo_slug}/src/{commit}/{path}](src/%7Bcommit%7D/%7Bpath%7D)
without having to know the name or SHA1 of the repo's main branch.

To create new commits, [POST to this endpoint](#post)
