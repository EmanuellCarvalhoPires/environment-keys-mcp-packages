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
tool: confluence_get_available_space_roles
title: "Confluence v2 - Get available space roles"
kind: request
request: "[[Confluence v2 - Get available space roles]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /space-roles · Get available space roles. Retrieves the available space roles. Available on tenants with Role-Based Access Control. Permissions required: Permission to access the Confluence site; if requesting a certain space's roles, permission to view the space. Writes data: no."
params:
  "space_id":
    type: string
    required: false
    description: "The space ID for which to filter available space roles; if empty, return all available space roles for the tenant."
  "role_type":
    type: string
    required: false
    description: "The space role type to filter results by."
  "principal_id":
    type: string
    required: false
    description: "The principal ID to filter results by. If specified, a principal-type must also be specified."
  "principal_type":
    type: string
    required: false
    description: "The principal type to filter results by. If specified, a principal-id must also be specified."
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
# confluence_get_available_space_roles

`GET /space-roles` — Get available space roles

- Request: [[Confluence v2 - Get available space roles]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
