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
tool: confluence_v1_get_watches_for_page
title: "Confluence v1 - Get watches for page"
kind: request
request: "[[Confluence v1 - Get watches for page]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/content/{id}/notification/child-created · Get watches for page. Returns the watches for a page. A user that watches a page will receive receive notifications when the page is updated. Writes data: no."
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
# confluence_v1_get_watches_for_page

`GET /wiki/rest/api/content/{id}/notification/child-created` — Get watches for page

- Request: [[Confluence v1 - Get watches for page]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
