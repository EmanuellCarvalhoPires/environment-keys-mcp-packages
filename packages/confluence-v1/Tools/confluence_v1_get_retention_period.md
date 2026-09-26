---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/audit
  - api/operation/list
  - api/effect/read
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_retention_period
title: "Confluence v1 - Get retention period"
kind: request
request: "[[Confluence v1 - Get retention period]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/audit/retention · Get retention period. Returns the retention period for records in the audit log. The retention period is how long an audit record is kept for, from creation date until it is deleted. Permissions required: 'Confluence Administrator' global permission. Writes data: no."
writes: false
expose: false
---
# confluence_v1_get_retention_period

`GET /wiki/rest/api/audit/retention` — Get retention period

- Request: [[Confluence v1 - Get retention period]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
