---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/permission-schemes
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_permission_scheme_grant
title: "Jira v3 - Get permission scheme grant"
kind: request
request: "[[Jira v3 - Get permission scheme grant]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/permissionscheme/{schemeId}/permission/{permissionId} · Get permission scheme grant. Returns a permission grant. Permissions required: Permission to access Jira. Writes data: no."
params:
  "schemeId":
    type: string
    required: true
    description: "The ID of the permission scheme."
  "permissionId":
    type: string
    required: true
    description: "The ID of the permission grant."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value."
writes: false
expose: false
---
# jira_get_permission_scheme_grant

`GET /rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}` — Get permission scheme grant

- Request: [[Jira v3 - Get permission scheme grant]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
