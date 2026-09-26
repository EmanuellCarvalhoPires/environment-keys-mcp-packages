---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/pullrequests"
category: "Pullrequests"
writes_data: false
tool_note: "[[bitbucket_list_pull_requests]]"
---
# Bitbucket - List pull requests

**List pull requests** — `GET /repositories/{workspace}/{repo_slug}/pullrequests`

- Run by the tool [[bitbucket_list_pull_requests]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests?state={{param:state}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `state` (query, string, optional) — Only return pull requests that are in this state. This parameter can be repeated.

## Original description

Returns all pull requests on the specified repository.

By default only open pull requests are returned. This can be controlled
using the `state` query parameter. To retrieve pull requests that are
in one of multiple states, repeat the `state` parameter for each
individual state.

This endpoint also supports filtering and sorting of the results. See
[filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.
