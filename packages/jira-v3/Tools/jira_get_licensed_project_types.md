---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-types
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_licensed_project_types
title: "Jira v3 - Get licensed project types"
kind: request
request: "[[Jira v3 - Get licensed project types]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/type/accessible · Get licensed project types. Returns all project types with a valid license. Writes data: no."
writes: false
expose: false
---
# jira_get_licensed_project_types

`GET /rest/api/3/project/type/accessible` — Get licensed project types

- Request: [[Jira v3 - Get licensed project types]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
