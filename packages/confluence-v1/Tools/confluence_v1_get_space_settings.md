---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-settings
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_space_settings
title: "Confluence v1 - Get space settings"
kind: request
request: "[[Confluence v1 - Get space settings]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/space/{spaceKey}/settings · Get space settings. Returns the settings of a space. Permissions required: 'View' permission for the space. Writes data: no."
params:
  "spaceKey":
    type: string
    required: true
    description: "The key of the space to be queried for its settings."
writes: false
expose: false
---
# confluence_v1_get_space_settings

`GET /wiki/rest/api/space/{spaceKey}/settings` — Get space settings

- Request: [[Confluence v1 - Get space settings]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
