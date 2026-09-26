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
path: "/rest/api/3/permissionscheme/{schemeId}"
category: "Permission schemes"
writes_data: true
tool_note: "[[jira_delete_permission_scheme]]"
---
# Jira v3 - Delete permission scheme

**Delete permission scheme** — `DELETE /rest/api/3/permissionscheme/{schemeId}`

- Run by the tool [[jira_delete_permission_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/permissionscheme/{{param:schemeId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `schemeId` (path, string, required) — The ID of the permission scheme being deleted.

## Original description

Deletes a permission scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
