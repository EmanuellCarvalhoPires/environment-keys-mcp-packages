---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/groups
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/group/user"
category: "Groups"
writes_data: true
tool_note: "[[jira_remove_user_from_group]]"
---
# Jira v3 - Remove user from group

**Remove user from group** — `DELETE /rest/api/3/group/user`

- Run by the tool [[jira_remove_user_from_group]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/group/user?groupname={{param:groupname}}&groupId={{param:groupId}}&username={{param:username}}&accountId={{param:accountId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `groupname` (query, string, optional) — As a group's name can change, use of groupId is recommended to identify a group. The name of the group. This parameter cannot be used with the groupId parameter.
- `groupId` (query, string, optional) — The ID of the group. This parameter cannot be used with the groupName parameter.
- `username` (query, string, optional) — This parameter is no longer available. See the deprecation notice for details.
- `accountId` (query, string, required) — The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5.

## Original description

Removes a user from a group.

**[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin* [group](https://confluence.atlassian.com/x/24xjL)).
