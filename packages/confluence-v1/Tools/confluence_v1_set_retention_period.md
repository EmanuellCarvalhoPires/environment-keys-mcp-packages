---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/audit
  - api/operation/update
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_set_retention_period
title: "Confluence v1 - Set retention period"
kind: request
request: "[[Confluence v1 - Set retention period]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · PUT /wiki/rest/api/audit/retention · Set retention period. Sets the retention period for records in the audit log. The retention period can be set to a maximum of 1 year. Permissions required: 'Confluence Administrator' global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_set_retention_period

`PUT /wiki/rest/api/audit/retention` — Set retention period

- Request: [[Confluence v1 - Set retention period]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
