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
path: "/workspaces/{workspace}/permissions"
category: "Workspaces"
writes_data: false
tool_note: "[[bitbucket_list_user_permissions_in_a_workspace]]"
---
# Bitbucket - List user permissions in a workspace

**List user permissions in a workspace** — `GET /workspaces/{workspace}/permissions`

- Run by the tool [[bitbucket_list_user_permissions_in_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/permissions?q={{param:q}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `q` (query, string, optional) — Query string to narrow down the response as per filtering and sorting.

## Original description

Returns the list of members in a workspace
and their permission levels.
Permission can be:
* `owner`
* `collaborator`
* `member`

**The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

**When you move your administration from Bitbucket Cloud to admin.atlassian.com, the following fields on
`workspace_membership` will no longer be present: `last_accessed` and `added_on`. See the
[deprecation announcement](/cloud/bitbucket/announcement-breaking-change-workspace-membership/).**

Results may be further [filtered](/cloud/bitbucket/rest/intro/#filtering) by
permission by adding the following query string parameters:

* `q=permission="owner"`
