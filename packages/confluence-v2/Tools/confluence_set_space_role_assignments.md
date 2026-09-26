---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-roles
  - api/operation/action
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_set_space_role_assignments
title: "Confluence v2 - Set space role assignments"
kind: request
request: "[[Confluence v2 - Set space role assignments]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /spaces/{id}/role-assignments · Set space role assignments. Sets space role assignments as specified in the payload. For each entry, if roleId is provided the principal is assigned to that role. If roleId is omitted, the role assignment for that principal is removed, if it exists. Available on tenants with Role-Based Access Control. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the space for which to retrieve assignments."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_set_space_role_assignments

`POST /spaces/{id}/role-assignments` — Set space role assignments

- Request: [[Confluence v2 - Set space role assignments]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
