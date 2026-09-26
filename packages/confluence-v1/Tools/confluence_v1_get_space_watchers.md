---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-watches
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_space_watchers
title: "Confluence v1 - Get space watchers"
kind: request
request: "[[Confluence v1 - Get space watchers]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/space/{spaceKey}/watch · Get space watchers. Returns a list of watchers of a space Writes data: no."
params:
  "spaceKey":
    type: string
    required: true
    description: "The key of the space to get watchers."
  "start":
    type: string
    required: false
    description: "The start point of the collection to return."
  "limit":
    type: string
    required: false
    description: "The limit of the number of items to return, this may be restricted by fixed system limits."
writes: false
expose: false
---
# confluence_v1_get_space_watchers

`GET /wiki/rest/api/space/{spaceKey}/watch` — Get space watchers

- Request: [[Confluence v1 - Get space watchers]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
