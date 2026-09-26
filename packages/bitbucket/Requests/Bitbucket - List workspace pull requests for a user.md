---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/workspaces/{workspace}/pullrequests/{selected_user}"
category: "Workspaces"
writes_data: false
tool_note: "[[bitbucket_list_workspace_pull_requests_for_a_user]]"
---
# Bitbucket - List workspace pull requests for a user

**List workspace pull requests for a user** — `GET /workspaces/{workspace}/pullrequests/{selected_user}`

- Run by the tool [[bitbucket_list_workspace_pull_requests_for_a_user]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/pullrequests/{{param:selected_user}}?state={{param:state}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `selected_user` (path, string, required) — Value of selecteduser in the path.
- `state` (query, string, optional) — Only return pull requests that are in this state. This parameter can be repeated.

## Original description

Returns all workspace pull requests authored by the specified user.

By default only open pull requests are returned. This can be controlled
using the `state` query parameter. To retrieve pull requests that are
in one of multiple states, repeat the `state` parameter for each
individual state.

This endpoint also supports filtering and sorting of the results. See
[filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.
