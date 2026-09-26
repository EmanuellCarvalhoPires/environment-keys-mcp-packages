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
tool: confluence_v1_get_restrictions
title: "Confluence v1 - Get restrictions"
kind: request
request: "[[Confluence v1 - Get restrictions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/content/{id}/restriction · Get restrictions. Returns the restrictions on a piece of content. Permissions required: Permission to view the content. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content to be queried for its restrictions."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the content restrictions to expand. By default, the following objects are expanded: restrictions.user, restrictions.group."
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
# confluence_v1_get_restrictions

`GET /wiki/rest/api/content/{id}/restriction` — Get restrictions

- Request: [[Confluence v1 - Get restrictions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
