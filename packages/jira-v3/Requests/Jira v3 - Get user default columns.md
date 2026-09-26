---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/users
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/user/columns"
category: "Users"
writes_data: false
tool_note: "[[jira_get_user_default_columns]]"
---
# Jira v3 - Get user default columns

**Get user default columns** — `GET /rest/api/3/user/columns`

- Run by the tool [[jira_get_user_default_columns]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/user/columns?accountId={{param:accountId}}&username={{param:username}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `accountId` (query, string, optional) — The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5.
- `username` (query, string, optional) — This parameter is no longer available See the deprecation notice for details.

## Original description

Returns the default [issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user. If `accountId` is not passed in the request, the calling user's details are returned.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLgl), to get the column details for any user.
 *  Permission to access Jira, to get the calling user's column details.
