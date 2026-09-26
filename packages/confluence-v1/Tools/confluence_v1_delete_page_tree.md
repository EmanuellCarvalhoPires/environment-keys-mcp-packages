---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/experimental
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_delete_page_tree
title: "Confluence v1 - Delete page tree"
kind: request
request: "[[Confluence v1 - Delete page tree]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · DELETE /wiki/rest/api/content/{id}/pageTree · Delete page tree. Moves a pagetree rooted at a page to the space's trash: - If the content's type is page and its status is current, it will be trashed including all its descendants. - For every other combination of content type and status, this API is not supported. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content which forms root of the page tree, to be deleted."
writes: true
expose: false
---
# confluence_v1_delete_page_tree

`DELETE /wiki/rest/api/content/{id}/pageTree` — Delete page tree

- Request: [[Confluence v1 - Delete page tree]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
