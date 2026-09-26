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
tool: confluence_v1_get_space_suggested_content_states
title: "Confluence v1 - Get space suggested content states"
kind: request
request: "[[Confluence v1 - Get space suggested content states]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/space/{spaceKey}/state · Get space suggested content states. Get content states that are suggested in the space. Permissions required: 'View' permission for the space. Writes data: no."
params:
  "spaceKey":
    type: string
    required: true
    description: "The key of the space to be queried for its content state settings."
writes: false
expose: false
---
# confluence_v1_get_space_suggested_content_states

`GET /wiki/rest/api/space/{spaceKey}/state` — Get space suggested content states

- Request: [[Confluence v1 - Get space suggested content states]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
