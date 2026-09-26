---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_fields
title: "Jira v3 - Get fields"
kind: request
request: "[[Jira v3 - Get fields]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/field · Get fields. Returns system and custom issue fields according to the following rules: Fields that cannot be added to the issue navigator are always returned. Fields that cannot be placed on an issue screen are always returned. Writes data: no."
writes: false
expose: false
---
# jira_get_fields

`GET /rest/api/3/field` — Get fields

- Request: [[Jira v3 - Get fields]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
