---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-restrictions
  - api/operation/get
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_restrictions_for_operation
title: "Confluence v1 - Get restrictions for operation"
kind: request
request: "[[Confluence v1 - Get restrictions for operation]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey} · Get restrictions for operation. Returns the restictions on a piece of content for a given operation (read or update). Permissions required: Permission to view the content. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content to be queried for its restrictions."
  "operationKey":
    type: string
    required: true
    description: "The operation type of the restrictions to be returned."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the content restrictions to expand. - restrictions.user returns the piece of content that the restrictions are applied to. Expanded by default."
  "start":
    type: string
    required: false
    description: "The starting index of the users and groups in the returned restrictions."
  "limit":
    type: string
    required: false
    description: "The maximum number of users and the maximum number of groups, in the returned restrictions, to return per page. Note, this may be restricted by fixed system limits."
writes: false
expose: false
---
# confluence_v1_get_restrictions_for_operation

`GET /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}` — Get restrictions for operation

- Request: [[Confluence v1 - Get restrictions for operation]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
