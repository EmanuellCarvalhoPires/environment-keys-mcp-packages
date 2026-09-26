---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/admin-key
  - api/operation/list
  - api/effect/read
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
tool: confluence_get_admin_key
title: "Confluence v2 - Get Admin Key"
kind: request
request: "[[Confluence v2 - Get Admin Key]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /admin-key · Get Admin Key. Returns information about the admin key if one is currently enabled for the calling user within the site. Permissions required: User must be an organization or site admin. Writes data: no."
writes: false
expose: false
---
# confluence_get_admin_key

`GET /admin-key` — Get Admin Key

- Request: [[Confluence v2 - Get Admin Key]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
