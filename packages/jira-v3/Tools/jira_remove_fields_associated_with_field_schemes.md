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
tool: jira_remove_fields_associated_with_field_schemes
title: "Jira v3 - Remove fields associated with field schemes"
kind: request
request: "[[Jira v3 - Remove fields associated with field schemes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/config/fieldschemes/fields · Remove fields associated with field schemes. Remove fields associated with field association schemes. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_remove_fields_associated_with_field_schemes

`DELETE /rest/api/3/config/fieldschemes/fields` — Remove fields associated with field schemes

- Request: [[Jira v3 - Remove fields associated with field schemes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
