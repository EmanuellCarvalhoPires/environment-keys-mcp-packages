---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/group
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_group
title: "Confluence v1 - Get group"
kind: request
request: "[[Confluence v1 - Get group]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/group/by-id · Get group. Returns a user group for a given group id. Permissions required: Permission to access the Confluence site ('Can use' global permission). Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The id of the group."
writes: false
expose: false
---
# confluence_v1_get_group

`GET /wiki/rest/api/group/by-id` — Get group

- Request: [[Confluence v1 - Get group]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
