---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/settings
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_look_and_feel_settings
title: "Confluence v1 - Get look and feel settings"
kind: request
request: "[[Confluence v1 - Get look and feel settings]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/settings/lookandfeel · Get look and feel settings. Returns the look and feel settings for the site or a single space. This includes attributes such as the color scheme, padding, and border radius. The look and feel settings for a space can be inherited from the global look and feel settings or provided by a theme. Writes data: no."
params:
  "spaceKey":
    type: string
    required: false
    description: "The key of the space for which the look and feel settings will be returned. If this is not set, only the global look and feel settings are returned."
writes: false
expose: false
---
# confluence_v1_get_look_and_feel_settings

`GET /wiki/rest/api/settings/lookandfeel` — Get look and feel settings

- Request: [[Confluence v1 - Get look and feel settings]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
