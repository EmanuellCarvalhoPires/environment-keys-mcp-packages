---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/permission-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}"
category: "Permission schemes"
writes_data: true
tool_note: "[[jira_delete_permission_scheme_grant]]"
---
# Jira v3 - Delete permission scheme grant

**Delete permission scheme grant** — `DELETE /rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}`

- Run by the tool [[jira_delete_permission_scheme_grant]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/permissionscheme/{{param:schemeId}}/permission/{{param:permissionId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `schemeId` (path, string, required) — The ID of the permission scheme to delete the permission grant from.
- `permissionId` (path, string, required) — The ID of the permission grant to delete.

## Original description

Deletes a permission grant from a permission scheme. See [About permission schemes and grants](../api-group-permission-schemes/#about-permission-schemes-and-grants) for more details.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
