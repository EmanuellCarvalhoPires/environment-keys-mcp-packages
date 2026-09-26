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
path: "/rest/api/3/user/columns"
category: "Users"
writes_data: true
tool_note: "[[jira_reset_user_default_columns]]"
---
# Jira v3 - Reset user default columns

**Reset user default columns** — `DELETE /rest/api/3/user/columns`

- Run by the tool [[jira_reset_user_default_columns]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/user/columns?accountId={{param:accountId}}&username={{param:username}}
Authorization: {{service.auth_token}}
```

## Parameters

- `accountId` (query, string, optional) — The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5.
- `username` (query, string, optional) — This parameter is no longer available. See the deprecation notice for details.

## Original description

Resets the default [ issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user to the system default. If `accountId` is not passed, the calling user's default columns are reset.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to set the columns on any user.
 *  Permission to access Jira, to set the calling user's columns.
