---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/users
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/user"
category: "Users"
writes_data: true
tool_note: "[[jira_delete_user]]"
---
# Jira v3 - Delete user

**Delete user** — `DELETE /rest/api/3/user`

- Run by the tool [[jira_delete_user]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/user?accountId={{param:accountId}}&username={{param:username}}&key={{param:key}}
Authorization: {{service.auth_token}}
```

## Parameters

- `accountId` (query, string, required) — The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5.
- `username` (query, string, optional) — This parameter is no longer available. See the deprecation notice for details.
- `key` (query, string, optional) — This parameter is no longer available. See the deprecation notice for details.

## Original description

Deletes a user. If the operation completes successfully then the user is removed from Jira's user base. This operation does not delete the user's Atlassian account.

**[Permissions](#permissions) required:** Site administration (that is, membership of the *site-admin* [group](https://confluence.atlassian.com/x/24xjL)).
