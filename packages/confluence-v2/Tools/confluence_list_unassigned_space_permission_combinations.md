---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-permission-transition
  - api/operation/list
  - api/effect/read
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
tool: confluence_list_unassigned_space_permission_combinations
title: "Confluence v2 - List unassigned space permission combinations"
kind: request
request: "[[Confluence v2 - List unassigned space permission combinations]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /space-permissions/transition/combinations · List unassigned space permission combinations. Lists the unique unassigned space permission combinations currently present on the tenant. Combinations that already map to a space role are filtered out server-side. Writes data: no."
params:
  "cursor":
    type: string
    required: false
    description: "Opaque cursor returned from a previous page in the cursor field of the response. Omit for the first page."
  "limit":
    type: string
    required: false
    description: "The maximum number of combinations to return per page. Requests outside the supported range return 400."
writes: false
expose: false
---
# confluence_list_unassigned_space_permission_combinations

`GET /space-permissions/transition/combinations` — List unassigned space permission combinations

- Request: [[Confluence v2 - List unassigned space permission combinations]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
