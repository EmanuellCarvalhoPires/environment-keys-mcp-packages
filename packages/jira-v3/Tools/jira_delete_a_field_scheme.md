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
tool: jira_delete_a_field_scheme
title: "Jira v3 - Delete a field scheme"
kind: request
request: "[[Jira v3 - Delete a field scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/config/fieldschemes/{id} · Delete a field scheme. Delete a specified field association scheme Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the field association scheme to delete."
writes: true
expose: false
---
# jira_delete_a_field_scheme

`DELETE /rest/api/3/config/fieldschemes/{id}` — Delete a field scheme

- Request: [[Jira v3 - Delete a field scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
