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
tool: confluence_v1_get_themes
title: "Confluence v1 - Get themes"
kind: request
request: "[[Confluence v1 - Get themes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/settings/theme · Get themes. Returns all themes, not including the default theme. Permissions required: None Writes data: no."
params:
  "start":
    type: string
    required: false
    description: "The starting index of the returned themes."
  "limit":
    type: string
    required: false
    description: "The maximum number of themes to return per page. Note, this may be restricted by fixed system limits."
writes: false
expose: false
---
# confluence_v1_get_themes

`GET /wiki/rest/api/settings/theme` — Get themes

- Request: [[Confluence v1 - Get themes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
