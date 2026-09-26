---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_remove_field_parameters
title: "Jira v3 - Remove field parameters"
kind: request
request: "[[Jira v3 - Remove field parameters]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/config/fieldschemes/fields/parameters · Remove field parameters. Remove field association parameters overrides for work types. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_remove_field_parameters

`DELETE /rest/api/3/config/fieldschemes/fields/parameters` — Remove field parameters

- Request: [[Jira v3 - Remove field parameters]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
