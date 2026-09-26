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
tool: confluence_v1_get_watches_for_space
title: "Confluence v1 - Get watches for space"
kind: request
request: "[[Confluence v1 - Get watches for space]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/content/{id}/notification/created · Get watches for space. Returns all space watches for the space that the content is in. A user that watches a space will receive receive notifications when any content in the space is updated. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content to be queried for its watches."
  "start":
    type: string
    required: false
    description: "The starting index of the returned watches."
  "limit":
    type: string
    required: false
    description: "The maximum number of watches to return per page. Note, this may be restricted by fixed system limits."
writes: false
expose: false
---
# confluence_v1_get_watches_for_space

`GET /wiki/rest/api/content/{id}/notification/created` — Get watches for space

- Request: [[Confluence v1 - Get watches for space]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
