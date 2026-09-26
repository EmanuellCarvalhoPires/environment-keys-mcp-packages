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
tool: confluence_v1_get_global_theme
title: "Confluence v1 - Get global theme"
kind: request
request: "[[Confluence v1 - Get global theme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/settings/theme/selected · Get global theme. Returns the globally assigned theme. Permissions required: None Writes data: no."
writes: false
expose: false
---
# confluence_v1_get_global_theme

`GET /wiki/rest/api/settings/theme/selected` — Get global theme

- Request: [[Confluence v1 - Get global theme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
