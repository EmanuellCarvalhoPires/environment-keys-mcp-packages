---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/settings
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_select_look_and_feel_settings
title: "Confluence v1 - Select look and feel settings"
kind: request
request: "[[Confluence v1 - Select look and feel settings]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · PUT /wiki/rest/api/settings/lookandfeel · Select look and feel settings. Sets the look and feel settings to the default (global) settings, the custom settings, or the current theme's settings for a space. The custom and theme settings can only be selected if there is already a theme set for a space. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_select_look_and_feel_settings

`PUT /wiki/rest/api/settings/lookandfeel` — Select look and feel settings

- Request: [[Confluence v1 - Select look and feel settings]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
