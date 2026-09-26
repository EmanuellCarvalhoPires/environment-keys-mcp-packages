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
tool: confluence_get_space_role_assignments
title: "Confluence v2 - Get space role assignments"
kind: request
request: "[[Confluence v2 - Get space role assignments]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /spaces/{id}/role-assignments · Get space role assignments. Retrieves the space role assignments. Available on tenants with Role-Based Access Control. Permissions required: Permission to view the space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the space for which to retrieve assignments."
  "role_id":
    type: string
    required: false
    description: "Filters the returned role assignments to the provided role ID."
  "role_type":
    type: string
    required: false
    description: "Filters the returned role assignments to the provided role type."
  "principal_id":
    type: string
    required: false
    description: "Filters the returned role assignments to the provided principal id. If specified, a principal-type must also be specified."
  "principal_type":
    type: string
    required: false
    description: "Filters the returned role assignments to the provided principal type. If specified, a principal-id must also be specified."
  "cursor":
    type: string
    required: false
    description: "Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results."
  "limit":
    type: string
    required: false
    description: "Maximum number of space roles to return. If more results exist, use the Link response header to retrieve a relative URL that will return the next set of results."
writes: false
expose: false
---
# confluence_get_space_role_assignments

`GET /spaces/{id}/role-assignments` — Get space role assignments

- Request: [[Confluence v2 - Get space role assignments]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
