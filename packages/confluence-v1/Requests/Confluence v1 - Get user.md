---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/users
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/user"
category: "Users"
writes_data: false
tool_note: "[[confluence_v1_get_user]]"
---
# Confluence v1 - Get user

**Get user** — `GET /wiki/rest/api/user`

- Run by the tool [[confluence_v1_get_user]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/user?accountId={{param:accountId}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `accountId` (query, string, required) — The account ID of the user. The accountId uniquely identifies the user across all Atlassian products. For example, 384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the user to expand. - operations returns the operations that the user is allowed to do.

## Original description

Returns a user. This includes information about the user, such as the
display name, account ID, profile picture, and more. The information returned may be
restricted by the user's profile visibility settings.

**Note:** to add, edit, or delete users in your organization, see the
[user management REST API](/cloud/admin/user-management/about/).

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
