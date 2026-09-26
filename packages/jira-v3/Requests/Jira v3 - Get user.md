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
path: "/rest/api/3/user"
category: "Users"
writes_data: false
tool_note: "[[jira_get_user]]"
---
# Jira v3 - Get user

**Get user** — `GET /rest/api/3/user`

- Run by the tool [[jira_get_user]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/user?accountId={{param:accountId}}&username={{param:username}}&key={{param:key}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `accountId` (query, string, optional) — The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5. Required.
- `username` (query, string, optional) — This parameter is no longer available. See the deprecation notice for details.
- `key` (query, string, optional) — This parameter is no longer available. See the deprecation notice for details.
- `expand` (query, string, optional) — Use expand to include additional information about users in the response. This parameter accepts a comma-separated list.

## Original description

Returns a user.

Privacy controls are applied to the response based on the user's preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

**[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
