---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/usage
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_tenant_usage_information
title: "Assets - Get tenant usage information"
kind: request
request: "[[Assets - Get tenant usage information]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /usage · Get tenant usage information. Retrieves comprehensive usage statistics for the current tenant including total object counts and a per-schema breakdown for billing and analytics. Writes data: no."
writes: false
expose: false
---
# assets_get_tenant_usage_information

`GET /usage` — Get tenant usage information

- Request: [[Assets - Get tenant usage information]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
