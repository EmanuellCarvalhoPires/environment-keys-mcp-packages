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
tool: confluence_get_version_details_for_blog_post_version
title: "Confluence v2 - Get version details for blog post version"
kind: request
request: "[[Confluence v2 - Get version details for blog post version]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /blogposts/{blogpost-id}/versions/{version-number} · Get version details for blog post version. Retrieves version details for the specified blog post and version number. Permissions required: Permission to view the blog post. Writes data: no."
params:
  "blogpost_id":
    type: string
    required: true
    description: "The ID of the blog post for which version details should be returned."
  "version_number":
    type: string
    required: true
    description: "The version number of the blog post to be returned."
writes: false
expose: false
---
# confluence_get_version_details_for_blog_post_version

`GET /blogposts/{blogpost-id}/versions/{version-number}` — Get version details for blog post version

- Request: [[Confluence v2 - Get version details for blog post version]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
