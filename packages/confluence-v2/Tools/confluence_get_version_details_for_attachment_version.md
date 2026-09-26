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
tool: confluence_get_version_details_for_attachment_version
title: "Confluence v2 - Get version details for attachment version"
kind: request
request: "[[Confluence v2 - Get version details for attachment version]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /attachments/{attachment-id}/versions/{version-number} · Get version details for attachment version. Retrieves version details for the specified attachment and version number. Permissions required: Permission to view the attachment. Writes data: no."
params:
  "attachment_id":
    type: string
    required: true
    description: "The ID of the attachment for which version details should be returned."
  "version_number":
    type: string
    required: true
    description: "The version number of the attachment to be returned."
writes: false
expose: false
---
# confluence_get_version_details_for_attachment_version

`GET /attachments/{attachment-id}/versions/{version-number}` — Get version details for attachment version

- Request: [[Confluence v2 - Get version details for attachment version]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
