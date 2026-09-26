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
tool: jira_delete_permission_scheme
title: "Jira v3 - Delete permission scheme"
kind: request
request: "[[Jira v3 - Delete permission scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/permissionscheme/{schemeId} · Delete permission scheme. Deletes a permission scheme. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "schemeId":
    type: string
    required: true
    description: "The ID of the permission scheme being deleted."
writes: true
expose: false
---
# jira_delete_permission_scheme

`DELETE /rest/api/3/permissionscheme/{schemeId}` — Delete permission scheme

- Request: [[Jira v3 - Delete permission scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
