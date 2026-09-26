---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_field_parameters
title: "Jira v3 - Get field parameters"
kind: request
request: "[[Jira v3 - Get field parameters]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/config/fieldschemes/{id}/fields/{fieldId}/parameters · Get field parameters. Retrieve field association parameters on a field association scheme Permissions required: Administer Jira global permission. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "the ID of the field association scheme to retrieve parameters for"
  "fieldId":
    type: string
    required: true
    description: "the ID of the field"
writes: false
expose: false
---
# jira_get_field_parameters

`GET /rest/api/3/config/fieldschemes/{id}/fields/{fieldId}/parameters` — Get field parameters

- Request: [[Jira v3 - Get field parameters]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
