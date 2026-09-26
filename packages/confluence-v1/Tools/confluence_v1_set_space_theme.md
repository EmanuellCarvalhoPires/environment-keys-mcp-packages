---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/themes
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_set_space_theme
title: "Confluence v1 - Set space theme"
kind: request
request: "[[Confluence v1 - Set space theme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · PUT /wiki/rest/api/space/{spaceKey}/theme · Set space theme. Sets the theme for a space. Note, if you want to reset the space theme to the default Confluence theme, use the 'Reset space theme' method instead of this method. Permissions required: 'Admin' permission for the space. Writes data: yes."
params:
  "spaceKey":
    type: string
    required: true
    description: "The key of the space to set the theme for."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_set_space_theme

`PUT /wiki/rest/api/space/{spaceKey}/theme` — Set space theme

- Request: [[Confluence v1 - Set space theme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
