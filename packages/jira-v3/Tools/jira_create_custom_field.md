---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_custom_field
title: "Jira v3 - Create custom field"
kind: request
request: "[[Jira v3 - Create custom field]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/field · Create custom field. Creates a custom field. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_custom_field

`POST /rest/api/3/field` — Create custom field

- Request: [[Jira v3 - Create custom field]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
