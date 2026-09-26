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
tool: confluence_get_version_details_for_footer_comment_version
title: "Confluence v2 - Get version details for footer comment version"
kind: request
request: "[[Confluence v2 - Get version details for footer comment version]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /footer-comments/{id}/versions/{version-number} · Get version details for footer comment version. Retrieves version details for the specified footer comment version. Permissions required: Permission to view the content of the page or blog post and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the footer comment for which version details should be returned."
  "version_number":
    type: string
    required: true
    description: "The version number of the footer comment to be returned."
writes: false
expose: false
---
# confluence_get_version_details_for_footer_comment_version

`GET /footer-comments/{id}/versions/{version-number}` — Get version details for footer comment version

- Request: [[Confluence v2 - Get version details for footer comment version]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
