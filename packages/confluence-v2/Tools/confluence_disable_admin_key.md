---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/admin-key
  - api/operation/delete
  - api/effect/write
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
tool: confluence_disable_admin_key
title: "Confluence v2 - Disable Admin Key"
kind: request
request: "[[Confluence v2 - Disable Admin Key]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · DELETE /admin-key · Disable Admin Key. Disables admin key access for the calling user within the site. Permissions required: User must be an organization or site admin. Writes data: yes."
writes: true
expose: false
---
# confluence_disable_admin_key

`DELETE /admin-key` — Disable Admin Key

- Request: [[Confluence v2 - Disable Admin Key]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
