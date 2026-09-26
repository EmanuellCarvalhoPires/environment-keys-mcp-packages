---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/filter-sharing
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/filter/{id}/permission/{permissionId}"
category: "Filter sharing"
writes_data: true
tool_note: "[[jira_delete_share_permission]]"
---
# Jira v3 - Delete share permission

**Delete share permission** — `DELETE /rest/api/3/filter/{id}/permission/{permissionId}`

- Run by the tool [[jira_delete_share_permission]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/filter/{{param:id}}/permission/{{param:permissionId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the filter.
- `permissionId` (path, string, required) — The ID of the share permission.

## Original description

Deletes a share permission from a filter.

**[Permissions](#permissions) required:** Permission to access Jira and the user must own the filter.
