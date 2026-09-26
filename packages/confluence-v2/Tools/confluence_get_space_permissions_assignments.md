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
tool: confluence_get_space_permissions_assignments
title: "Confluence v2 - Get space permissions assignments"
kind: request
request: "[[Confluence v2 - Get space permissions assignments]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /spaces/{id}/permissions · Get space permissions assignments. Returns space permission assignments for a specific space. Permissions required: Permission to view the space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the space to be returned."
  "cursor":
    type: string
    required: false
    description: "Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results."
  "limit":
    type: string
    required: false
    description: "Maximum number of assignments to return. If more results exist, use the Link response header to retrieve a relative URL that will return the next set of results."
writes: false
expose: false
---
# confluence_get_space_permissions_assignments

`GET /spaces/{id}/permissions` — Get space permissions assignments

- Request: [[Confluence v2 - Get space permissions assignments]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
