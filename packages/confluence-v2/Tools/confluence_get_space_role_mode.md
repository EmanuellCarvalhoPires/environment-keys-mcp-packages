---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-roles
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_space_role_mode
title: "Confluence v2 - Get space role mode"
kind: request
request: "[[Confluence v2 - Get space role mode]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /space-role-mode · Get space role mode. Retrieves the space role mode. Available on tenants with Role-Based Access Control. Permissions required: Permission to access the Confluence site ('Can use' global permission). Writes data: no."
writes: false
expose: false
---
# confluence_get_space_role_mode

`GET /space-role-mode` — Get space role mode

- Request: [[Confluence v2 - Get space role mode]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
