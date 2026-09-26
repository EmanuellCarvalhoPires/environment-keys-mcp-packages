---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-restrictions
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_restrictions_by_operation
title: "Confluence v1 - Get restrictions by operation"
kind: request
request: "[[Confluence v1 - Get restrictions by operation]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/content/{id}/restriction/byOperation · Get restrictions by operation. Returns restrictions on a piece of content by operation. This method is similar to Get restrictions except that the operations are properties of the return object, rather than items in a results array. Permissions required: Permission to view the content. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content to be queried for its restrictions."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the content restrictions to expand. - restrictions.user returns the piece of content that the restrictions are applied to. Expanded by default."
writes: false
expose: false
---
# confluence_v1_get_restrictions_by_operation

`GET /wiki/rest/api/content/{id}/restriction/byOperation` — Get restrictions by operation

- Request: [[Confluence v1 - Get restrictions by operation]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
