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
tool: confluence_bulk_assign_space_permission_roles
title: "Confluence v2 - Bulk assign space permission roles"
kind: request
request: "[[Confluence v2 - Bulk assign space permission roles]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /space-permissions/transition/role-assignments · Bulk assign space permission roles. Bulk assigns roles for one or more permission combination IDs obtained from the space permission combinations. Supports targeting all spaces, specific spaces, or excluding specific spaces. Permissions required: User must be a Confluence administrator. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_bulk_assign_space_permission_roles

`POST /space-permissions/transition/role-assignments` — Bulk assign space permission roles

- Request: [[Confluence v2 - Bulk assign space permission roles]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
