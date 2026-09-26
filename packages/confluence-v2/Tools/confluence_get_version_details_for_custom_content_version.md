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
tool: confluence_get_version_details_for_custom_content_version
title: "Confluence v2 - Get version details for custom content version"
kind: request
request: "[[Confluence v2 - Get version details for custom content version]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /custom-content/{custom-content-id}/versions/{version-number} · Get version details for custom content version. Retrieves version details for the specified custom content and version number. Permissions required: Permission to view the page. Writes data: no."
params:
  "custom_content_id":
    type: string
    required: true
    description: "The ID of the custom content for which version details should be returned."
  "version_number":
    type: string
    required: true
    description: "The version number of the custom content to be returned."
writes: false
expose: false
---
# confluence_get_version_details_for_custom_content_version

`GET /custom-content/{custom-content-id}/versions/{version-number}` — Get version details for custom content version

- Request: [[Confluence v2 - Get version details for custom content version]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
