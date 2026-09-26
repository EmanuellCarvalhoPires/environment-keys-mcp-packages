---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-states
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_content_state_settings_for_space
title: "Confluence v1 - Get content state settings for space"
kind: request
request: "[[Confluence v1 - Get content state settings for space]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/space/{spaceKey}/state/settings · Get content state settings for space. Get object describing whether content states are allowed at all, if custom content states or space content states are restricted, and a list of space content states allowed for the space if they are not restricted. Permissions required: 'Admin' permission for the space. Writes data: no."
params:
  "spaceKey":
    type: string
    required: true
    description: "The key of the space to be queried for its content state settings."
writes: false
expose: false
---
# confluence_v1_get_content_state_settings_for_space

`GET /wiki/rest/api/space/{spaceKey}/state/settings` — Get content state settings for space

- Request: [[Confluence v1 - Get content state settings for space]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
