---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/permissions
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_bulk_permissions
title: "Jira v3 - Get bulk permissions"
kind: request
request: "[[Jira v3 - Get bulk permissions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/permissions/check · Get bulk permissions. Returns: for a list of global permissions, the global permissions granted to a user. for a list of project permissions and lists of projects and issues, for each project permission a list of the projects and issues a user can access or manipulate. Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_get_bulk_permissions

`POST /rest/api/3/permissions/check` — Get bulk permissions

- Request: [[Jira v3 - Get bulk permissions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
