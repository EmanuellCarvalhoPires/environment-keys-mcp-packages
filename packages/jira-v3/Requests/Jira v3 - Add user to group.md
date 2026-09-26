---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/groups
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/group/user"
category: "Groups"
writes_data: true
tool_note: "[[jira_add_user_to_group]]"
---
# Jira v3 - Add user to group

**Add user to group** — `POST /rest/api/3/group/user`

- Run by the tool [[jira_add_user_to_group]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/group/user?groupname={{param:groupname}}&groupId={{param:groupId}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `groupname` (query, string, optional) — As a group's name can change, use of groupId is recommended to identify a group. The name of the group. This parameter cannot be used with the groupId parameter.
- `groupId` (query, string, optional) — The ID of the group. This parameter cannot be used with the groupName parameter.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "accountId": "5b10ac8d82e05b22cc7d4ef5"
}
```

## Original description

Adds a user to a group.

**[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin* [group](https://confluence.atlassian.com/x/24xjL)).
