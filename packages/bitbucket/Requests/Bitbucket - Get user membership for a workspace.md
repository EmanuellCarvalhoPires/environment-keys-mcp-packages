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
path: "/workspaces/{workspace}/members/{member}"
category: "Workspaces"
writes_data: false
tool_note: "[[bitbucket_get_user_membership_for_a_workspace]]"
---
# Bitbucket - Get user membership for a workspace

**Get user membership for a workspace** — `GET /workspaces/{workspace}/members/{member}`

- Run by the tool [[bitbucket_get_user_membership_for_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/members/{{param:member}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `member` (path, string, required) — Value of member in the path.

## Original description

Returns the workspace membership, which includes
a `User` object for the member and a `Workspace` object
for the requested workspace.
