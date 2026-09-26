---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-roles
  - api/operation/create
  - api/effect/write
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
tool: confluence_create_a_space_role
title: "Confluence v2 - Create a space role"
kind: request
request: "[[Confluence v2 - Create a space role]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /space-roles · Create a space role. Create a space role. Available on tenants with Role-Based Access Control. Permissions required: User must be an organization or site admin. Connect and Forge app users are not authorized to access this resource. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_a_space_role

`POST /space-roles` — Create a space role

- Request: [[Confluence v2 - Create a space role]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
