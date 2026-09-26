---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-roles
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_space_role_by_id
title: "Confluence v2 - Get space role by ID"
kind: request
request: "[[Confluence v2 - Get space role by ID]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /space-roles/{id} · Get space role by ID. Retrieves the space role by ID. Available on tenants with Role-Based Access Control. Permissions required: Permission to access the Confluence site. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the space role to retrieve."
writes: false
expose: false
---
# confluence_get_space_role_by_id

`GET /space-roles/{id}` — Get space role by ID

- Request: [[Confluence v2 - Get space role by ID]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
