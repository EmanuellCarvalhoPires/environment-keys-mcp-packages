---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_fields_associated_with_field_schemes
title: "Jira v3 - Update fields associated with field schemes"
kind: request
request: "[[Jira v3 - Update fields associated with field schemes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/config/fieldschemes/fields · Update fields associated with field schemes. Update fields associated with field association schemes. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_fields_associated_with_field_schemes

`PUT /rest/api/3/config/fieldschemes/fields` — Update fields associated with field schemes

- Request: [[Jira v3 - Update fields associated with field schemes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
