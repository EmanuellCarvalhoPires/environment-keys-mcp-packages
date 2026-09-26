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
path: "/wiki/rest/api/group/by-id"
category: "Group"
writes_data: true
tool_note: "[[confluence_v1_delete_user_group]]"
---
# Confluence v1 - Delete user group

**Delete user group** — `DELETE /wiki/rest/api/group/by-id`

- Run by the tool [[confluence_v1_delete_user_group]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/group/by-id?id={{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (query, string, required) — Id of the group to delete.

## Original description

Delete user group.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
User must be a site admin.
