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
path: "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments"
category: "Pullrequests"
writes_data: false
tool_note: "[[bitbucket_list_comments_on_a_pull_request]]"
---
# Bitbucket - List comments on a pull request

**List comments on a pull request** — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments`

- Run by the tool [[bitbucket_list_comments_on_a_pull_request]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests/{{param:pull_request_id}}/comments
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `pull_request_id` (path, string, required) — Value of pullrequestid in the path.

## Original description

Returns a paginated list of the pull request's comments.

This includes both global, inline comments and replies.

The default sorting is oldest to newest and can be overridden with
the `sort` query parameter.

This endpoint also supports filtering and sorting of the results. See
[filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more
details.
