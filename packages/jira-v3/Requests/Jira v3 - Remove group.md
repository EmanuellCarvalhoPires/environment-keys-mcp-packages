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
path: "/rest/api/3/group"
category: "Groups"
writes_data: true
tool_note: "[[jira_remove_group]]"
---
# Jira v3 - Remove group

**Remove group** — `DELETE /rest/api/3/group`

- Run by the tool [[jira_remove_group]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/group?groupname={{param:groupname}}&groupId={{param:groupId}}&swapGroup={{param:swapGroup}}&swapGroupId={{param:swapGroupId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `groupname` (query, string, optional) — Query parameter groupname.
- `groupId` (query, string, optional) — The ID of the group. This parameter cannot be used with the groupname parameter.
- `swapGroup` (query, string, optional) — As a group's name can change, use of swapGroupId is recommended to identify a group. The group to transfer restrictions to. Only comments and worklogs are transferred.
- `swapGroupId` (query, string, optional) — The ID of the group to transfer restrictions to. Only comments and worklogs are transferred. If restrictions are not transferred, comments and worklogs are inaccessible after the deletion.

## Original description

Deletes a group.

**[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin* strategic [group](https://confluence.atlassian.com/x/24xjL)).
