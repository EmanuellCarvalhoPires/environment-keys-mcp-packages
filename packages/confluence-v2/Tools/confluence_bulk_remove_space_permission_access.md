---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-permission-transition
  - api/operation/action
  - api/effect/write
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
tool: confluence_bulk_remove_space_permission_access
title: "Confluence v2 - Bulk remove space permission access"
kind: request
request: "[[Confluence v2 - Bulk remove space permission access]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /space-permissions/transition/access-removals · Bulk remove space permission access. Bulk removes access for one or more permission combination IDs obtained from the space permission combinations. This removes all space permissions for the specified combinations across the targeted spaces. Permissions required: User must be a Confluence administrator. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_bulk_remove_space_permission_access

`POST /space-permissions/transition/access-removals` — Bulk remove space permission access

- Request: [[Confluence v2 - Bulk remove space permission access]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
