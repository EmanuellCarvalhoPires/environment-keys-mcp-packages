---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/settings
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_system_info
title: "Confluence v1 - Get system info"
kind: request
request: "[[Confluence v1 - Get system info]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/settings/systemInfo · Get system info. Returns the system information for the Confluence Cloud tenant. This information is used by Atlassian. Permissions required: Permission to access the Confluence site ('Can use' global permission). Writes data: no."
writes: false
expose: false
---
# confluence_v1_get_system_info

`GET /wiki/rest/api/settings/systemInfo` — Get system info

- Request: [[Confluence v1 - Get system info]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
