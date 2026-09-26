---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/users
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/user/groups"
category: "Users"
writes_data: false
tool_note: "[[jira_get_user_groups]]"
---
# Jira v3 - Get user groups

**Get user groups** — `GET /rest/api/3/user/groups`

- Run by the tool [[jira_get_user_groups]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/user/groups?accountId={{param:accountId}}&username={{param:username}}&key={{param:key}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `accountId` (query, string, required) — The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5.
- `username` (query, string, optional) — This parameter is no longer available. See the deprecation notice for details.
- `key` (query, string, optional) — This parameter is no longer available. See the deprecation notice for details.

## Original description

Returns the groups to which a user belongs.

**[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
