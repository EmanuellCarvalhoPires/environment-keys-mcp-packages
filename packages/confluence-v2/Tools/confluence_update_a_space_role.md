---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-roles
  - api/operation/update
  - api/effect/write
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
tool: confluence_update_a_space_role
title: "Confluence v2 - Update a space role"
kind: request
request: "[[Confluence v2 - Update a space role]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · PUT /space-roles/{id} · Update a space role. Update a space role. Available on tenants with Role-Based Access Control. Permissions required: User must be an organization or site admin. Connect and Forge app users are not authorized to access this resource. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "Id of the space role"
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_update_a_space_role

`PUT /space-roles/{id}` — Update a space role

- Request: [[Confluence v2 - Update a space role]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
