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
path: "/wiki/rest/api/user/memberof"
category: "Users"
writes_data: false
tool_note: "[[confluence_v1_get_group_memberships_for_user]]"
---
# Confluence v1 - Get group memberships for user

**Get group memberships for user** — `GET /wiki/rest/api/user/memberof`

- Run by the tool [[confluence_v1_get_group_memberships_for_user]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/user/memberof?accountId={{param:accountId}}&start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `accountId` (query, string, required) — The account ID of the user. The accountId uniquely identifies the user across all Atlassian products. For example, 384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192.
- `start` (query, string, optional) — The starting index of the returned groups.
- `limit` (query, string, optional) — The maximum number of groups to return per page. Note, this may be restricted by fixed system limits.

## Original description

Returns the groups that a user is a member of.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
