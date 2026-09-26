---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/settings
  - api/operation/action
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_update_look_and_feel_settings
title: "Confluence v1 - Update look and feel settings"
kind: request
request: "[[Confluence v1 - Update look and feel settings]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/settings/lookandfeel/custom · Update look and feel settings. Updates the look and feel settings for the site or for a single space. If custom settings exist, they are updated. If no custom settings exist, then a set of custom settings is created. Writes data: yes."
params:
  "spaceKey":
    type: string
    required: false
    description: "The key of the space for which the look and feel settings will be updated. If this is not set, the global look and feel settings will be updated."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_update_look_and_feel_settings

`POST /wiki/rest/api/settings/lookandfeel/custom` — Update look and feel settings

- Request: [[Confluence v1 - Update look and feel settings]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
