---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/settings
  - api/operation/delete
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_reset_look_and_feel_settings
title: "Confluence v1 - Reset look and feel settings"
kind: request
request: "[[Confluence v1 - Reset look and feel settings]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · DELETE /wiki/rest/api/settings/lookandfeel/custom · Reset look and feel settings. Resets the custom look and feel settings for the site or a single space. This changes the values of the custom settings to be the same as the default settings. It does not change which settings (default or custom) are selected. Writes data: yes."
params:
  "spaceKey":
    type: string
    required: false
    description: "The key of the space for which the look and feel settings will be reset. If this is not set, the global look and feel settings will be reset."
writes: true
expose: false
---
# confluence_v1_reset_look_and_feel_settings

`DELETE /wiki/rest/api/settings/lookandfeel/custom` — Reset look and feel settings

- Request: [[Confluence v1 - Reset look and feel settings]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
