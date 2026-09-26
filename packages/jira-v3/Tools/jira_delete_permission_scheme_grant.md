---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/permission-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_permission_scheme_grant
title: "Jira v3 - Delete permission scheme grant"
kind: request
request: "[[Jira v3 - Delete permission scheme grant]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/permissionscheme/{schemeId}/permission/{permissionId} · Delete permission scheme grant. Deletes a permission grant from a permission scheme. See About permission schemes and grants for more details. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "schemeId":
    type: string
    required: true
    description: "The ID of the permission scheme to delete the permission grant from."
  "permissionId":
    type: string
    required: true
    description: "The ID of the permission grant to delete."
writes: true
expose: false
---
# jira_delete_permission_scheme_grant

`DELETE /rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}` — Delete permission scheme grant

- Request: [[Jira v3 - Delete permission scheme grant]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
