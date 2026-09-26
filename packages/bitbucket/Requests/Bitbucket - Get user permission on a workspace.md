---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/user/workspaces/{workspace}/permission"
category: "Workspaces"
writes_data: false
tool_note: "[[bitbucket_get_user_permission_on_a_workspace]]"
---
# Bitbucket - Get user permission on a workspace

**Get user permission on a workspace** — `GET /user/workspaces/{workspace}/permission`

- Run by the tool [[bitbucket_get_user_permission_on_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/user/workspaces/{{service.workspace}}/permission
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns the caller's effective role; as in, the highest level of privilege
the caller has for the workspace.
If the calling user is a member of multiple groups with distinct roles, only the
highest level is returned.

Permissions can be:

* `owner`
* `create-project`
* `collaborator` (deprecated; see this
[deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/) for more details)
* `member`
