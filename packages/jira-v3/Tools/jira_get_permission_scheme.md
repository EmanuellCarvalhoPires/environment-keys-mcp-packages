---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/permission-schemes
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_permission_scheme
title: "Jira v3 - Get permission scheme"
kind: request
request: "[[Jira v3 - Get permission scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/permissionscheme/{schemeId} · Get permission scheme. Returns a permission scheme. Permissions required: Permission to access Jira. Writes data: no."
params:
  "schemeId":
    type: string
    required: true
    description: "The ID of the permission scheme to return."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value."
writes: false
expose: false
---
# jira_get_permission_scheme

`GET /rest/api/3/permissionscheme/{schemeId}` — Get permission scheme

- Request: [[Jira v3 - Get permission scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
