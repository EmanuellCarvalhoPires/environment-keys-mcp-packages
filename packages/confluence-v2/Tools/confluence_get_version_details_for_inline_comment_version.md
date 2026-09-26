---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/version
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_version_details_for_inline_comment_version
title: "Confluence v2 - Get version details for inline comment version"
kind: request
request: "[[Confluence v2 - Get version details for inline comment version]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /inline-comments/{id}/versions/{version-number} · Get version details for inline comment version. Retrieves version details for the specified inline comment version. Permissions required: Permission to view the content of the page or blog post and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the inline comment for which version details should be returned."
  "version_number":
    type: string
    required: true
    description: "The version number of the inline comment to be returned."
writes: false
expose: false
---
# confluence_get_version_details_for_inline_comment_version

`GET /inline-comments/{id}/versions/{version-number}` — Get version details for inline comment version

- Request: [[Confluence v2 - Get version details for inline comment version]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
