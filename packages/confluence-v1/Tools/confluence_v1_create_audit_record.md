---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/audit
  - api/operation/create
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_create_audit_record
title: "Confluence v1 - Create audit record"
kind: request
request: "[[Confluence v1 - Create audit record]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/audit · Create audit record. Creates a record in the audit log. Permissions required: 'Confluence Administrator' global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_create_audit_record

`POST /wiki/rest/api/audit` — Create audit record

- Request: [[Confluence v1 - Create audit record]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
