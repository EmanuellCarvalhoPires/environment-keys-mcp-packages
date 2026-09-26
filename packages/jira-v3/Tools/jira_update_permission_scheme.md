---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/permission-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_permission_scheme
title: "Jira v3 - Update permission scheme"
kind: request
request: "[[Jira v3 - Update permission scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/permissionscheme/{schemeId} · Update permission scheme. Updates a permission scheme. Below are some important things to note when using this resource: If a permissions list is present in the request, then it is set in the permission scheme, overwriting all existing grants. Writes data: yes."
params:
  "schemeId":
    type: string
    required: true
    description: "The ID of the permission scheme to update."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_permission_scheme

`PUT /rest/api/3/permissionscheme/{schemeId}` — Update permission scheme

- Request: [[Jira v3 - Update permission scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
