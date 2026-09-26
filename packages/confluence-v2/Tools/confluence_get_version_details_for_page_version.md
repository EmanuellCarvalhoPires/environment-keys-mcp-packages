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
tool: confluence_get_version_details_for_page_version
title: "Confluence v2 - Get version details for page version"
kind: request
request: "[[Confluence v2 - Get version details for page version]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /pages/{page-id}/versions/{version-number} · Get version details for page version. Retrieves version details for the specified page and version number. Permissions required: Permission to view the page. Writes data: no."
params:
  "page_id":
    type: string
    required: true
    description: "The ID of the page for which version details should be returned."
  "version_number":
    type: string
    required: true
    description: "The version number of the page to be returned."
writes: false
expose: false
---
# confluence_get_version_details_for_page_version

`GET /pages/{page-id}/versions/{version-number}` — Get version details for page version

- Request: [[Confluence v2 - Get version details for page version]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
