---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-children-and-descendants
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_content_descendants
title: "Confluence v1 - Get content descendants"
kind: request
request: "[[Confluence v1 - Get content descendants]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/content/{id}/descendant · Get content descendants. Returns a map of the descendants of a piece of content. This is similar to Get content children, except that this method returns child pages at all levels, rather than just the direct child pages. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content to be queried for its descendants."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the children to expand, where: - attachment returns all attachments for the content. - comments returns all comments for the content."
writes: false
expose: false
---
# confluence_v1_get_content_descendants

`GET /wiki/rest/api/content/{id}/descendant` — Get content descendants

- Request: [[Confluence v1 - Get content descendants]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
