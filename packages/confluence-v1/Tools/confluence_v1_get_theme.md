---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/themes
  - api/operation/get
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_theme
title: "Confluence v1 - Get theme"
kind: request
request: "[[Confluence v1 - Get theme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/settings/theme/{themeKey} · Get theme. Returns a theme. This includes information about the theme name, description, and icon. Permissions required: None Writes data: no."
params:
  "themeKey":
    type: string
    required: true
    description: "The key of the theme to be returned."
writes: false
expose: false
---
# confluence_v1_get_theme

`GET /wiki/rest/api/settings/theme/{themeKey}` — Get theme

- Request: [[Confluence v1 - Get theme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
