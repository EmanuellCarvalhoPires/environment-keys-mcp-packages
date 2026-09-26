---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-roles
  - api/operation/delete
  - api/effect/write
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
tool: confluence_delete_a_space_role
title: "Confluence v2 - Delete a space role"
kind: request
request: "[[Confluence v2 - Delete a space role]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · DELETE /space-roles/{id} · Delete a space role. Delete a space role Available on tenants with Role-Based Access Control. Permissions required: User must be an organization or site admin. Connect and Forge app users are not authorized to access this resource. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "Id of the space role"
writes: true
expose: false
---
# confluence_delete_a_space_role

`DELETE /space-roles/{id}` — Delete a space role

- Request: [[Confluence v2 - Delete a space role]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
