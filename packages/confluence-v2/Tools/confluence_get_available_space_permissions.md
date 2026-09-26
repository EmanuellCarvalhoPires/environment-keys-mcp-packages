---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-permissions
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_available_space_permissions
title: "Confluence v2 - Get available space permissions"
kind: request
request: "[[Confluence v2 - Get available space permissions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /space-permissions · Get available space permissions. Retrieves the available space permissions. Available on tenants with Role-Based Access Control. Permissions required: Permission to access the Confluence site. Writes data: no."
params:
  "cursor":
    type: string
    required: false
    description: "Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results."
  "limit":
    type: string
    required: false
    description: "Maximum number of space permissions to return. If more results exist, use the Link response header to retrieve a relative URL that will return the next set of results."
writes: false
expose: false
---
# confluence_get_available_space_permissions

`GET /space-permissions` — Get available space permissions

- Request: [[Confluence v2 - Get available space permissions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
