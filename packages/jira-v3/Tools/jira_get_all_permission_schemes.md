---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/permission-schemes
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_all_permission_schemes
title: "Jira v3 - Get all permission schemes"
kind: request
request: "[[Jira v3 - Get all permission schemes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/permissionscheme · Get all permission schemes. Returns all permission schemes. About permission schemes and grants A permission scheme is a collection of permission grants. A permission grant consists of a holder and a permission. Writes data: no."
params:
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value."
writes: false
expose: false
---
# jira_get_all_permission_schemes

`GET /rest/api/3/permissionscheme` — Get all permission schemes

- Request: [[Jira v3 - Get all permission schemes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
