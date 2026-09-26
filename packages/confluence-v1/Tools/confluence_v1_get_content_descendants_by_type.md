---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-children-and-descendants
  - api/operation/get
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_content_descendants_by_type
title: "Confluence v1 - Get content descendants by type"
kind: request
request: "[[Confluence v1 - Get content descendants by type]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/content/{id}/descendant/{type} · Get content descendants by type. Returns all descendants of a given type, for a piece of content. This is similar to Get content children by type, except that this method returns child pages at all levels, rather than just the direct child pages. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content to be queried for its descendants."
  "type":
    type: string
    required: true
    description: "The type of descendants to return."
  "depth":
    type: string
    required: false
    description: "Filter the results to descendants upto a desired level of the content. Note, the maximum value supported is 100. root level of the content means immediate (level 1) descendants of the type requested."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the content to expand. - childTypes.all returns whether the content has attachments, comments, or child pages/whiteboards."
  "start":
    type: string
    required: false
    description: "The starting index of the returned content."
  "limit":
    type: string
    required: false
    description: "The maximum number of content to return per page. Note, this may be restricted by fixed system limits."
writes: false
expose: false
---
# confluence_v1_get_content_descendants_by_type

`GET /wiki/rest/api/content/{id}/descendant/{type}` — Get content descendants by type

- Request: [[Confluence v1 - Get content descendants by type]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
