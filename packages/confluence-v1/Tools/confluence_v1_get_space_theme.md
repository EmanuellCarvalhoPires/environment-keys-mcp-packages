---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/themes
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_space_theme
title: "Confluence v1 - Get space theme"
kind: request
request: "[[Confluence v1 - Get space theme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/space/{spaceKey}/theme · Get space theme. Returns the theme selected for a space, if one is set. If no space theme is set, this means that the space is inheriting the global look and feel settings. Permissions required: ‘View’ permission for the space. Writes data: no."
params:
  "spaceKey":
    type: string
    required: true
    description: "The key of the space to be queried for its theme."
writes: false
expose: false
---
# confluence_v1_get_space_theme

`GET /wiki/rest/api/space/{spaceKey}/theme` — Get space theme

- Request: [[Confluence v1 - Get space theme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
