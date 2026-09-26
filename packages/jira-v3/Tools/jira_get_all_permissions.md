---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/permissions
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_all_permissions
title: "Jira v3 - Get all permissions"
kind: request
request: "[[Jira v3 - Get all permissions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/permissions · Get all permissions. Returns all permissions, including: global permissions. project permissions. global permissions added by plugins. This operation can be accessed anonymously. Permissions required: None. Writes data: no."
writes: false
expose: false
---
# jira_get_all_permissions

`GET /rest/api/3/permissions` — Get all permissions

- Request: [[Jira v3 - Get all permissions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
