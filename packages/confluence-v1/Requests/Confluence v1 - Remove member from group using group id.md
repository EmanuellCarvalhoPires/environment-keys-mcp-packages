---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/group
  - api/operation/delete
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: DELETE
path: "/wiki/rest/api/group/userByGroupId"
category: "Group"
writes_data: true
tool_note: "[[confluence_v1_remove_member_from_group_using_group_id]]"
---
# Confluence v1 - Remove member from group using group id

**Remove member from group using group id** — `DELETE /wiki/rest/api/group/userByGroupId`

- Run by the tool [[confluence_v1_remove_member_from_group_using_group_id]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/group/userByGroupId?groupId={{param:groupId}}&accountId={{param:accountId}}&key={{param:key}}&username={{param:username}}
Authorization: {{service.auth_token}}
```

## Parameters

- `groupId` (query, string, required) — Id of the group whose membership is updated.
- `accountId` (query, string, required) — The account ID of the user. The accountId uniquely identifies the user across all Atlassian products. For example, 384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192.
- `key` (query, string, optional) — This parameter is no longer available and will be removed from the documentation soon. Use accountId instead. See the deprecation notice for details.
- `username` (query, string, optional) — This parameter is no longer available and will be removed from the documentation soon. Use accountId instead. See the deprecation notice for details.

## Original description

Remove user as a member from a group.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
User must be a site admin.
