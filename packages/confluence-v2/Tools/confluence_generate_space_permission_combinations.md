---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-permission-transition
  - api/operation/action
  - api/effect/write
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
tool: confluence_generate_space_permission_combinations
title: "Confluence v2 - Generate space permission combinations"
kind: request
request: "[[Confluence v2 - Generate space permission combinations]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /space-permissions/transition/combinations · Generate space permission combinations. Submits a task to refresh the space permission combinations in the database, which identifies all unique permission combinations across the site. This provides permission combination IDs that can be used with the assign-roles and remove-access endpoints. Writes data: yes."
writes: true
expose: false
---
# confluence_generate_space_permission_combinations

`POST /space-permissions/transition/combinations` — Generate space permission combinations

- Request: [[Confluence v2 - Generate space permission combinations]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
