---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/themes
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_reset_space_theme
title: "Confluence v1 - Reset space theme"
kind: request
request: "[[Confluence v1 - Reset space theme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · DELETE /wiki/rest/api/space/{spaceKey}/theme · Reset space theme. Resets the space theme. This means that the space will inherit the global look and feel settings Permissions required: 'Admin' permission for the space. Writes data: yes."
params:
  "spaceKey":
    type: string
    required: true
    description: "The key of the space to reset the theme for."
writes: true
expose: false
---
# confluence_v1_reset_space_theme

`DELETE /wiki/rest/api/space/{spaceKey}/theme` — Reset space theme

- Request: [[Confluence v1 - Reset space theme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
