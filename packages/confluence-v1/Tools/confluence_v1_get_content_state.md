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
tool: confluence_v1_get_content_state
title: "Confluence v1 - Get content state"
kind: request
request: "[[Confluence v1 - Get content state]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/content/{id}/state · Get content state. Gets the current content state of the draft or current version of content. To specify the draft version, set the parameter status to draft, otherwise archived or current will get the relevant published state. Permissions required: Permission to view the content. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The id of the content whose content state is of interest."
  "status":
    type: string
    required: false
    description: "Set status to one of [current,draft,archived]. Default value is current."
writes: false
expose: false
---
# confluence_v1_get_content_state

`GET /wiki/rest/api/content/{id}/state` — Get content state

- Request: [[Confluence v1 - Get content state]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
