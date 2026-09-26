---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-permissions
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: DELETE
path: "/wiki/rest/api/space/{spaceKey}/permission/{id}"
category: "Space permissions"
writes_data: true
tool_note: "[[confluence_v1_remove_a_space_permission]]"
---
# Confluence v1 - Remove a space permission

**Remove a space permission** — `DELETE /wiki/rest/api/space/{spaceKey}/permission/{id}`

- Run by the tool [[confluence_v1_remove_a_space_permission]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/space/{{param:spaceKey}}/permission/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `spaceKey` (path, string, required) — The key of the space to be queried for its content.
- `id` (path, string, required) — Id of the permission to be deleted.

## Original description

Removes a space permission. Note that removing Read Space permission for a user or group will remove all
the space permissions for that user or group.

Note: Apps cannot access this REST resource - including when utilizing user impersonation.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Admin' permission for the space.
