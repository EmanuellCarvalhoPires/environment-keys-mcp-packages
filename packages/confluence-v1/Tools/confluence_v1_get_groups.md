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
tool: confluence_v1_get_groups
title: "Confluence v1 - Get groups"
kind: request
request: "[[Confluence v1 - Get groups]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/group · Get groups. Returns all user groups. The returned groups are ordered alphabetically in ascending order by group name. Permissions required: Permission to access the Confluence site ('Can use' global permission). Writes data: no."
params:
  "start":
    type: string
    required: false
    description: "The starting index of the returned groups."
  "limit":
    type: string
    required: false
    description: "The maximum number of groups to return per page. Note, this may be restricted by fixed system limits."
  "accessType":
    type: string
    required: false
    description: "The group permission level for which to filter results."
writes: false
expose: false
---
# confluence_v1_get_groups

`GET /wiki/rest/api/group` — Get groups

- Request: [[Confluence v1 - Get groups]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
