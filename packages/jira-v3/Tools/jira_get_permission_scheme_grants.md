---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/permission-schemes
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_permission_scheme_grants
title: "Jira v3 - Get permission scheme grants"
kind: request
request: "[[Jira v3 - Get permission scheme grants]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/permissionscheme/{schemeId}/permission · Get permission scheme grants. Returns all permission grants for a permission scheme. Permissions required: Permission to access Jira. Writes data: no."
params:
  "schemeId":
    type: string
    required: true
    description: "The ID of the permission scheme."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value."
writes: false
expose: false
---
# jira_get_permission_scheme_grants

`GET /rest/api/3/permissionscheme/{schemeId}/permission` — Get permission scheme grants

- Request: [[Jira v3 - Get permission scheme grants]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
