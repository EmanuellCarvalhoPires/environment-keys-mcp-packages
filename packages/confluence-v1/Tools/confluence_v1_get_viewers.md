---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/analytics
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_viewers
title: "Confluence v1 - Get viewers"
kind: request
request: "[[Confluence v1 - Get viewers]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/analytics/content/{contentId}/viewers · Get viewers. Get the total number of distinct viewers a piece of content has. Writes data: no."
params:
  "contentId":
    type: string
    required: true
    description: "The ID of the content to get the viewers for."
  "fromDate":
    type: string
    required: false
    description: "The number of views for the content since the date."
writes: false
expose: false
---
# confluence_v1_get_viewers

`GET /wiki/rest/api/analytics/content/{contentId}/viewers` — Get viewers

- Request: [[Confluence v1 - Get viewers]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
